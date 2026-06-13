# ⚔️ Active Directory Domain Reconnaissance & Advanced Enumeration Master Cheatsheet

This cheatsheet provides a comprehensive, highly categorized defensive and offensive blueprint for identifying hidden configurations, operational directory metadata leaks, and data disclosures within an Active Directory ecosystem.

---

## 🚪 1. System Access & Shell Validation (WinRM Mechanics)

### Core Command

```bash
evil-winrm -i 10.0.2.3 -u labuser -p 'P@ssw0rd123!'

```

### Option & Parameter Breakdown

* `-i`: Target IP Address. Specifies the network endpoint hosting the Web Services-Management (WS-Management) listener.
* `-u`: Username context. The security principal credential under which the remote session request runs.
* `-p`: Plaintext password string. Used to build the initial cryptographic negotiation blocks.

### Under-the-Hood Logic

WinRM uses ports **5985 (HTTP)** and **5986 (HTTPS)**. Execution sets up an authenticated SOAP-over-HTTP connection. Once initialized, the target server spawns an instance of `wsmprovhost.exe` under the specified user identity, passing input/output via standard WinRM serialization layers.

> [!WARNING]
> **The WinRM Authorization Edge Case:** > If you possess valid credentials but face a `WinRMAuthorizationError` (such as trying to connect directly to a Domain Controller), the user context lacks interactive remote management privileges on that explicit node. Network ports will appear wide open, and credentials will validate globally, but the server side will abruptly close the execution thread during user token evaluation.

---

### 🚀 Advanced Variations & Strategic Alternatives

#### Alternative A: NetExec / CrackMapExec Subnet Assessment (Multi-Node Validation)

```bash
nxc winrm 10.0.2.0/24 -u labuser -p 'P@ssw0rd123!'

```

* **Operational Value:** Evaluates an entire CIDR block for interactive execution endpoints simultaneously instead of checking individual machines one-by-one.

#### Alternative B: DCOM-Based Windows Management Instrumentation (`wmiexec.py`)

```bash
wmiexec.py PENTESTLAB.local/labuser:'P@ssw0rd123!'@10.0.2.4

```

* **Situation Where ONLY This Works:** When network administrators implement stringent Group Policies (GPOs) that explicitly disable WS-Management services or block WinRM ports host-wide, but leave standard administrative access active. `wmiexec.py` pivots away from HTTP/HTTPS channels entirely. It utilizes RPC/DCOM over **Port 135** and dynamic high ports to talk directly to the WMI Win32 provider sub-system, executing actions stealthily via `WmiPrvSE.exe`.

---

## 📡 2. Directory Root Object Reconnaissance (ADSI Engine)

### Core Script

```powershell
$Domain = [ADSI]"LDAP://RootDSE"
$RootDN = $Domain.defaultNamingContext
$ADObject = [ADSI]"LDAP://$RootDN"
$ADObject.RefreshCache(@("*", "+"))
$ADObject | Select-Object -Property *

```

### Option & Parameter Breakdown

* `[ADSI]"LDAP://RootDSE"`: Binds directly to the Root Directory Service Entry. This exposes critical environmental metadata without needing to know domain-specific naming paths beforehand.
* `.defaultNamingContext`: Dynamically reads and extracts the active, top-level Distinguished Name partition (e.g., `DC=PENTESTLAB,DC=local`).
* `.RefreshCache(@("*", "+"))`: The critical data extraction accelerator. The `*` string forces loading of standard schema values, while the `+` character forces construction and delivery of **operational/hidden fields**.

### Under-the-Hood Logic

Standard LDAP queries save network bandwidth by omitting dynamic attributes calculated on the fly by Domain Controllers. Forcing a programmatic cache refresh with the `+` wild-card tells the database parser to compile extended data attributes like `adminDescription`.

---

### 🚀 Advanced Variations & Strategic Alternatives

#### Alternative A: Broad Root Directory Searcher Wrapper (`[adsisearcher]`)

```powershell
$Searcher = [adsisearcher]""
$Searcher.SearchBase = "LDAP://RootDSE"
$Searcher.FindOne().Properties

```

* **Operational Value:** Returns standard operational metadata properties instantly without instantiating explicit cache manipulation memory streams.

#### Alternative B: Raw Python Over-the-Wire LDAP Query (`ldap3` Matrix)

```python
import ldap3
s = ldap3.Server('10.0.2.4', get_info=ldap3.ALL)
c = ldap3.Connection(s, user='PENTESTLAB\\labuser', password='P@ssw0rd123!', auto_bind=True)
c.search('DC=PENTESTLAB,DC=local', '(objectClass=domain)', attributes=['*','+'])
print(c.entries)

```

* **Situation Where ONLY This Works:** If a target workstation features restrictive PowerShell Constrained Language Mode (CLM) constraints or active Antimalware Scan Interface (AMSI) script block scanning, running native `[ADSI]` accelerators will trigger immediate administrative alerts.
* Executing an unmanaged python script or pre-compiled binary communicates straight over network sockets directly to **Port 389**. This bypasses local AMSI engines and endpoint execution telemetry entirely.

---

## 🔍 3. Targeted Service Account Sweep Loop (User Objects)

### Core Script

```powershell
$Accounts = @("svc_deploy", "svc_web", "SvcBackup", "SvcWeb")
foreach ($Name in $Accounts) {
    $Searcher = [ADSISearcher]"(&(objectClass=user)(cn=$Name))"
    $Result = $Searcher.FindOne()
    if ($Result) {
        $DN = $Result.Properties.distinguishedname[0]
        $AccountObject = [ADSI]"LDAP://$DN"
        $AccountObject.RefreshCache(@("*", "+"))
        $AccountObject | Select-Object -Property *
    }
}

```

### Option & Parameter Breakdown

* `(&(objectClass=user)(cn=$Name))`: Custom Boolean LDAP filter logic string. Returns directory entities that simultaneously match the target class (`user`) AND feature a common name matching the current tracking variable loop.
* `.FindOne()`: Directs the underlying search engine API to halt processing and return the single closest matching schema object index, minimizing network overhead.

### Under-the-Hood Logic

The query looks up relative common account tags and resolves their absolute database paths (`DistinguishedName`). This enables operators to identify configurations like Kerberos Constrained Delegation flags (`msDS-AllowedToDelegateTo`) or explicit Service Principal Names (`servicePrincipalName`).

---

### 🚀 Advanced Variations & Strategic Alternatives

#### Alternative A: Native AD Module Targeted Query Pipeline

```powershell
Get-ADUser -Filter "CN -like 'svc*'" -Properties * | Select-Object SamAccountName, servicePrincipalName, msDS-AllowedToDelegateTo, description

```

* **Operational Value:** Utilizes official Microsoft administration tooling parameters to dump standard attack vectors quickly in readable row formats.

#### Alternative B: Non-Standard Advanced Substring Filtering via ADSI Core

```powershell
$Searcher = [ADSISearcher]"(&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))"
$Searcher.PropertiesToLoad.AddRange(@("samaccountname","serviceprincipalname","msds-allowedtodelegateto"))
$Searcher.FindAll() | ForEach-Object { $_.Properties }

```

* **Situation Where ONLY This Works:** If the target environment blocks administrative tool modules (missing `Microsoft.ActiveDirectory.Management.dll`) and security engineers audit for account enumeration queries via simple string detection rules (e.g., alert on explicit account loops looking for `svc_web`).
* This alternative uses a bitwise LDAP search filter (`1.2.840.113556.1.4.803:=2`) to query for **all enabled accounts** across the environment while requesting only specific exploitation fields (`serviceprincipalname`). This identifies Kerberoasting and Delegation paths in a single execution block without explicit loops.

---

## 🏛️ 4. Privileged Container Auditing (LDAP Protocol Level)

### Core Command

```bash
ldapsearch -H ldap://10.0.2.4 \
  -x \
  -D "CN=labuser,CN=Users,DC=PENTESTLAB,DC=local" \
  -w 'P@ssw0rd123!' \
  -b "DC=PENTESTLAB,DC=local" \
  "(&(objectCategory=group)(|(cn=Domain Admins)(cn=Enterprise Admins)(cn=Backup Operators)))" \
  "*" "+"

```

### Option & Parameter Breakdown

* `-H ldap://...`: Uniform Resource Identifier. Defines the connection protocol scheme and target domain controller destination.
* `-x`: Simple Authentication option. Instructs the application to negotiate direct plaintext verification bounds over standard channels rather than complex SASL frameworks.
* `-D`: Bind Distinguished Name. Sets the explicit administrative identity track executing the search path.
* `-b`: Search Base DN. Defines the container node root location from which recursive search paths propagate downward.
* `"*" "+"`: Dual operational request tags ensuring both basic attribute keys and hidden/constructed property entries (like `info`) are returned.

---

### 🚀 Advanced Variations & Strategic Alternatives

#### Alternative A: Automated Domain Group Ingestion via NetExec LDAP Module

```bash
nxc ldap 10.0.2.4 -u labuser -p 'P@ssw0rd123!' --groups

```

* **Operational Value:** Authenticates and converts raw schema group information strings into high-visibility tables immediately inside your terminal console window.

#### Alternative B: Token Groups Operational Evaluation over ADSI (`tokenGroups` Extraction)

```powershell
$UserDN = (New-Object System.DirectoryServices.DirectorySearcher("(&(sAMAccountName=labuser))")).FindOne().Path
$User = [ADSI]"$UserDN"
$User.RefreshCache(@("tokenGroups"))
foreach ($SIDByte in $User.tokenGroups) {
    $SID = New-Object System.Security.Principal.SecurityIdentifier ($SIDByte, 0)
    $SID.Translate([System.Security.Principal.NTAccount])
}

```

* **Situation Where ONLY This Works:** When administrators implement Nested Group memberships (e.g., `labuser` is inside a group called `App-Admins`, which itself is nested inside `Domain Admins`).
* If you run standard `ldapsearch` lookups querying simple direct group memberships (`member`), the user will not appear under the target group object list. This programmatic alternative pulls the dynamic **`tokenGroups`** operational attribute directly from the user's live login token. This forces the Domain Controller to recursively compute all primary, secondary, and nested group assignments, revealing your true effective access.

---

## 💻 5. Host Registry Architecture Evaluation

### Core Command

```powershell
Get-ItemProperty -Path HKLM:\SOFTWARE\HolbertonLab

```

### Option & Parameter Breakdown

* `Get-ItemProperty`: Retrieves the explicit parameters and metadata key string values housed inside a target folder node.
* `-Path HKLM:\SOFTWARE\...`: Directs the PowerShell registry provider path context engine to parse data out of the `HKEY_LOCAL_MACHINE` hive.

### Under-the-Hood Logic

The registry functions as a hierarchical configuration database. While structural objects inside the `HKLM\SOFTWARE` path typically manage software parameters, third-party deployment configurations or legacy scripts often leave unencrypted text information strings exposed here.

---

### 🚀 Advanced Variations & Strategic Alternatives

#### Alternative A: Native Legacy Binary Direct Query (`reg.exe`)

```cmd
reg query HKLM\SOFTWARE\HolbertonLab /s

```

* **Operational Value:** Performs recursive key scans from a raw legacy command shell (`cmd.exe`) without invoking PowerShell runspaces.

#### Alternative B: CIM Engine WMI Interfacing (`StdRegProv`)

```powershell
Invoke-CimMethod -ClassName StdRegProv -MethodName EnumValues -Arguments @{hDefKey=[uint32]2147483650; sSubKeyName="SOFTWARE\HolbertonLab"}

```

* **Situation Where ONLY This Works:** When Defensive Endpoint Detection & Response (EDR) agents or intense Script Block Logging monitor common commands like `Get-ItemProperty` or alert on direct process creations of `reg.exe` by non-standard users.
* This advanced approach contacts the Common Information Model (CIM) interface layer, routing the execution context directly through the trusted core system instrumentation channel (`WmiPrvSE.exe`). The OS returns the desired registry data while bypassing local command-line monitoring filters.

---

## 📊 6. Comprehensive Omni-Sweep User Property Audit

### Core Command

```powershell
Get-ADUser -Filter * -Properties * | Select-Object SamAccountName, Title, Description, Info, Comment, adminDescription | Format-List

```

### Option & Parameter Breakdown

* `-Filter *`: Requests every record matching the object schema category inside the target partition.
* `-Properties *`: Forces the retrieval of non-standard attributes that are normally ignored during basic user listings.
* `Select-Object ...`: Isolates specific fields frequently misused for storing cleartext descriptions, old password records, or setup notes.

---

### 🚀 Advanced Variations & Strategic Alternatives

#### Alternative A: Targeted Active Directory Service Interfaces Pipeline Lookups

```powershell
([adsisearcher]"objectClass=user").FindAll() | ForEach-Object { New-Object PSObject -Property @{ Name = $_.Properties.samaccountname[0]; Desc = $_.Properties.description[0]; Comm = $_.Properties.comment[0] } }

```

* **Operational Value:** Extracts standard freeform comment property locations cleanly on hosts where official administration modules are absent.

#### Alternative B: Dynamic Search Filter Isolation via Kerberos Pre-Authentication Configuration Check

```powershell
Get-ADUser -LDAPFilter "(userAccountControl:1.2.840.113556.1.4.803:=4194304)" -Properties * | Select-Object SamAccountName, Comment

```

* **Situation Where ONLY This Works:** When hunting for specific, highly exploitable accounts in massive directory environments with tens of thousands of users where standard broad dumps (`-Filter *`) take hours and overwhelm memory limits.
* This filter checks the User Account Control (UAC) bitmask specifically for the `DONT_REQ_PREAUTH` flag (**4194304**). This isolates highly vulnerable accounts vulnerable to immediate AS-REP Roasting attacks while extracting their `Comment` data blocks in a single, targeted transaction.

---

## 🧠 Environmental Attack Matrix & Tactical Decision Guide

The table below maps real-world environmental restrictions to their corresponding tactical workarounds and exploit mechanics:

| If Your Environment Presents... | The Primary Tooling Fail Path Is... | Pivot Your Action Strategy To... | Underlying Exploit Vector / Tactical Objective |
| --- | --- | --- | --- |
| **Interactive Login Restrictions on Domain Controllers** | Standard WinRM connections fail with explicit `AuthorizationError` alerts. | Use **LDAP Directory Extraction via Port 389** (`ldapsearch`). | Pulls hidden schema data attributes directly from directory data structures without requiring terminal host shells. |
| **Active Kerberoasting Targets (`servicePrincipalName`)** | Offline dictionary cracking of user password hashes retrieved from standard accounts. | Perform an **Offline TGS Ticket Extraction Sweep**. | Allows operators to pull vulnerable ticket blocks and attempt offline brute-force cracking of weak password fields. |
| **Kerberos Constrained Delegation Configuration Flaws** | Accounts containing explicit destinations inside `msDS-AllowedToDelegateTo`. | Execute **S4U2self / S4U2proxy Impersonation Pivots**. | Forges authentication credentials to impersonate high-privilege administrative tokens to targeted endpoints. |
| **Insecure Registry Permissions over Shared Hosts** | Hardcoded environment tokens left inside custom software nodes. | Run **WMI Core Infrastructure Probes** (`StdRegProv`). | Extracts sensitive string assets hidden inside common registries by targeting default read boundaries. |
| **Missing Active Directory Administrative Tooling Modules** | `Get-ADUser` binaries or library paths return missing reference errors. | Use **Native ADSI Search Wrappers** (`[adsisearcher]`). | Interlaces with basic operational library runspaces present on all Windows baselines by default. |
| **Strict Process Auditing or Command String Alerts** | Command paths logging `reg.exe` or standard query parameters trigger security alerts. | Execute **Unmanaged Sockets Programming** (`ldap3`). | Shifts interaction models to lower network protocol stacks, bypassing host monitoring tools. |
| **Nested Security Group Membership Configurations** | Lookups querying explicit group attributes fail to show true group layout. | Query the **`tokenGroups` Dynamic Property**. | Computes complete, real-time recursive membership paths across complex directory systems. |
