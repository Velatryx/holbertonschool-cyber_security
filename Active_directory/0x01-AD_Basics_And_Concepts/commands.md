# 📂 commands.md

## 🚪 1. Remote Management & Shell Footholds

### Evil-WinRM Interactive Shell

```bash
evil-winrm -i 10.0.2.3 -u labuser -p 'P@ssw0rd123!'

```

### NetExec Subnet WinRM Verification (Mass Sweep)

```bash
nxc winrm 10.0.2.0/24 -u labuser -p 'P@ssw0rd123!'

```

### Impacket WMI Execution (Protocol Pivot via Port 135/445)

```bash
wmiexec.py PENTESTLAB.local/labuser:'P@ssw0rd123!'@10.0.2.4

```

---

## 📡 2. Directory Root Object Reconnaissance

### Native PowerShell ADSI RootDSE Cache Blast

```powershell
$Domain = [ADSI]"LDAP://RootDSE"
$RootDN = $Domain.defaultNamingContext
$ADObject = [ADSI]"LDAP://$RootDN"
$ADObject.RefreshCache(@("*", "+"))
$ADObject | Select-Object -Property *

```

### Lightweight ADSI Searcher Root Grab

```powershell
$Searcher = [adsisearcher]""
$Searcher.SearchBase = "LDAP://RootDSE"
$Searcher.FindOne().Properties

```

### Linux-Based Over-The-Wire Root Object Query

```bash
ldapsearch -H ldap://10.0.2.4 \
  -x \
  -D "CN=labuser,CN=Users,DC=PENTESTLAB,DC=local" \
  -w 'P@ssw0rd123!' \
  -b "DC=PENTESTLAB,DC=local" \
  "(objectClass=domain)" \
  "*流通" "+"

```

---

## 🔍 3. Service Account sweeps & Object Mapping

### Automated ADSI Service Account Extraction Loop

```powershell
$Accounts = @("svc_deploy", "svc_web", "SvcBackup", "SvcWeb")
foreach ($Name in $Accounts) {
    $Searcher = [ADSISearcher]"(&(objectClass=user)(cn=$Name))"
    $Result = $Searcher.FindOne()
    if ($Result) {
        $DN = $Result.Properties.distinguishedname[0]
        $AccountObject = [ADSI]"LDAP://$DN"
        $AccountObject.RefreshCache(@("*", "+"))
        Write-Output "==================== [ $Name ] ===================="
        $AccountObject | Select-Object -Property *
    }
}

```

### Native ActiveDirectory Module Service Account Enumeration

```powershell
Get-ADUser -Filter "CN -like 'svc*'" -Properties * | Select-Object SamAccountName, servicePrincipalName, msDS-AllowedToDelegateTo, description, info

```

### Target Filter for Enabled Profiles (Bypassing Name Restrictions)

```powershell
$Searcher = [ADSISearcher]"(&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))"
$Searcher.PropertiesToLoad.AddRange(@("samaccountname","serviceprincipalname","msds-allowedtodelegateto"))
$Searcher.FindAll() | ForEach-Object { $_.Properties }

```

---

## 🏛️ 4. Privileged Container Auditing

### High-Privilege Group Extraction via LDAP

```bash
ldapsearch -H ldap://10.0.2.4 \
  -x \
  -D "CN=labuser,CN=Users,DC=PENTESTLAB,DC=local" \
  -w 'P@ssw0rd123!' \
  -b "DC=PENTESTLAB,DC=local" \
  "(&(objectCategory=group)(|(cn=Domain Admins)(cn=Enterprise Admins)(cn=Backup Operators)))" \
  "*" "+"

```

### NetExec Automated Group Triage Engine

```bash
nxc ldap 10.0.2.4 -u labuser -p 'P@ssw0rd123!' --groups

```

### Programmatic Recursive Token Group/Nested Membership Evaluation

```powershell
$UserDN = (New-Object System.DirectoryServices.DirectorySearcher("(&(sAMAccountName=labuser))")).FindOne().Path
$User = [ADSI]"$UserDN"
$User.RefreshCache(@("tokenGroups"))
foreach ($SIDByte in $User.tokenGroups) {
    $SID = New-Object System.Security.Principal.SecurityIdentifier ($SIDByte, 0)
    $SID.Translate([System.Security.Principal.NTAccount])
}

```

---

## 💻 5. Windows Host Registry Reconnaissance

### Target Key Property Extraction Cmdlet

```powershell
Get-ItemProperty -Path HKLM:\SOFTWARE\HolbertonLab

```

### Full Local Machine Software Node Directory Tree Map

```powershell
Get-ChildItem -Path HKLM:\SOFTWARE

```

### Native Command Line Registry Query (No PowerShell Footprint)

```cmd
reg query HKLM\SOFTWARE\HolbertonLab /s

```

### CIM Provider WMI Remote Hive Lookup

```powershell
Invoke-CimMethod -ClassName StdRegProv -MethodName EnumValues -Arguments @{hDefKey=[uint32]2147483650; sSubKeyName="SOFTWARE\HolbertonLab"}

```

---

## 📊 6. Comprehensive Extended Attribute Auditing

### Active Directory Domain Omni-Sweep Module Pipeline

```powershell
Get-ADUser -Filter * -Properties * | Select-Object SamAccountName, Title, Description, Info, Comment, adminDescription | Format-List

```

### Standard User Object Asset Hunting via ADSI

```powershell
([adsisearcher]"objectClass=user").FindAll() | ForEach-Object { New-Object PSObject -Property @{ Name = $_.Properties.samaccountname[0]; Desc = $_.Properties.description[0]; Comm = $_.Properties.comment[0] } }

```

### AS-REP Roasting Target Sweep with Account Parameter Extraction

```powershell
Get-ADUser -LDAPFilter "(userAccountControl:1.2.840.113556.1.4.803:=4194304)" -Properties * | Select-Object SamAccountName, Comment, description

```
