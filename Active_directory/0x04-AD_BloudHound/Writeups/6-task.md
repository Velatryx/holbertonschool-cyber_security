## Phase 1: SMB Share Content Enumeration via NetExec

### Our mission is: Authenticate against the domain controller using low-privileged credentials to map and list files within the globally readable SYSVOL share

Blueprint:
`nxc smb [1. Target IP] -u [2. Username] -p '[3. Password]' --share [4. Share Name] --dir '[5. Relative Directory Path]'`

Command:

```bash
nxc smb 192.168.56.20 -u bh_intern -p 'User@2025!' --share SYSVOL --dir 'PENTESTLAB.local\scripts'

```

Explanation:

* `nxc smb`: Invokes the Server Message Block protocol engine inside NetExec to interact with network filesystems.
* `-u bh_intern -p 'User@2025!'`: Authenticated context utilizing default low-privilege domain user parameters.
* `--share SYSVOL`: Targets the system volume repository, which contains global policies and scripts automatically synchronized across all domain controllers.
* `--dir 'PENTESTLAB.local\scripts'`: Restricts the structural directory traversal path to the designated login and maintenance scripts subdirectory tree.

Brief Explanation:

> "Active Directory deployments dynamically maintain the `SYSVOL` share to broadcast Group Policy Objects (GPOs) and startup/logon configurations to network endpoints. Because this directory requires a baseline read access level for all domain objects, it regularly becomes a target for credential hunting. Querying the structure natively with a low-privileged identity reveals target configuration scripts and unencrypted text templates."

---

## Phase 2: Targeted File Extraction via NetExec

### Our mission is: Download high-value information repositories directly from the remote SMB directory architecture onto the local working environment

Blueprint:
`nxc smb [1. Target IP] -u [2. Username] -p '[3. Password]' --share [4. Share Name] --get-file '[5. Remote File Path]' [6. Local Destination Name]`

Command:

```bash
nxc smb 192.168.56.20 -u bh_intern -p 'User@2025!' --share SYSVOL --get-file 'PENTESTLAB.local\scripts\bh_notes.txt' bh_notes.txt

```

Explanation:

* `--get-file 'PENTESTLAB.local\scripts\bh_notes.txt' bh_notes.txt`: Commands NetExec to establish an explicit data-transfer stream, pulling down the specific target text item and writing it locally to disk.

Brief Explanation:

> "Isolate identified non-standard documentation assets such as `bh_notes.txt` out of the operational script directory. Extracting files over SMB using automation engines facilitates offline analysis and safeguards against potential session loss during live assessment windows."

---

## Phase 3: Interactive SMB Share Interrogation via Native smbclient

### Our mission is: Establish an interactive command-line session within the remote share to manually audit policy trees and directory structures

Blueprint:
`smbclient //[1. Target IP or Hostname]/[2. Share Name] -U [3. Username]@[4. Domain]`

Command:

```bash
smbclient //192.168.56.20/SYSVOL -U bh_intern@PENTESTLAB.local

```

Explanation:

* `smbclient //192.168.56.20/SYSVOL`: Utilizes the standard Samba interactive network subsystem to open a live session targeting the system volume storage node.
* `-U bh_intern@PENTESTLAB.local`: Formats user parameters under a fully qualified user principal format to prompt for immediate password-based interactive session binding.

Brief Explanation:

> "Interactive session creation via `smbclient` offers a manual alternative to script automation. This method enables direct exploration of core Group Policy storage tracks (such as the standard GUID container files under the `Policies` tree) and live directory inspection using standard shell-like navigation strings."

---

## Data Exfiltration & Target Leak Analysis

Parsing the harvested file contents reveals critical configuration notes, graph database endpoints, and active authentication parameters.

### Recovered System Flag

> **`BHFLAG6{SYSVOL_SMB_SH4R3_L34K_BONUS}`**
