### Our first mission is: Enumerate Active Directory identities and discover hidden account parameters via the RPC protocol

First, I did some basic things.

Blueprint:
`rpcclient -U 'username%pass' IP`

```bash
rpcclient -U 'student%password1234' 192.168.56.20
```

Once authenticated, I ran:

`enumdomusers`: to list all the users with their RID's.

Then:

`queryuser <RID>`: to display information about a specific user, that sometimes LDAP do not show.


---

### To avoid hustle by querying the users one by one, I used this loop to list all user details at once.

Blueprint:
`rpcclient -U '[1. Username]%[2. Password]' [3. Target IP] -c "[4. Core RPC Command Operations]"`

Command:

```bash
for rid in $(rpcclient -U 'student%password1234' 192.168.56.20 -c "enumdomusers" | awk -F'0x' '{print $2}' | awk '{print $1}'); do
    echo "[+] RID: 0x$rid"
    rpcclient -U 'student%password1234' 192.168.56.20 -c "queryuser 0x$rid"
done

```

Explanation:

`rpcclient`: A specialized tool utility used to execute client-side MS-RPC functions, communicating over SMB port 445 to interact with administrative pipes like SAMR (Security Accounts Manager Remote).

`-U 'student%password1234'`: Supplies the authentication bundle directly using the format `username%password`, circumventing standard interactive authentication prompts.

`-c "enumdomusers"`: Instructs `rpcclient` to connect, run the internal SAMR command to list all domain objects categorized as user structures, print their corresponding Relative Identifiers (RIDs), and close the pipe connection.

`awk -F'0x' '{print $2}' | awk '{print $1}'`: A programmatic text-parsing filter chain that cuts each string at the hex prefix `0x` and isolates raw hexadecimal string sequences representing the RIDs.

`"queryuser 0x$rid"`: A specific MS-RPC operation that queries the Domain Controller for the comprehensive internal structural layout block of a given identity, pulling properties that are often absent or restricted in LDAP.

Brief Explanation:

> "Establish an authenticated MS-RPC console connection to the domain controller at 192.168.56.20 using legitimate domain student credentials. Execute an initial sweeping scan via the SAMR pipe to map out every single user profile and isolate their hex-encoded Relative Identifier (RID) values. Feed those IDs dynamically into a shell execution loop to repeatedly punch queries back through the pipe, demanding the absolute structural field-dump of every individual account database row. This targets native operational data placeholders that standard directory access methods hide from unprivileged users."

Interaction Workflow & Retrieval:

```text
[+] RID: 0x1f4]
        User Name   :   Administrator
        Full Name   :
        Description :   Built-in account for administering the computer/domain
        Logon Time               :      Sun, 21 Jun 2026 13:52:22 EDT
        Password last set Time   :      Thu, 29 Jan 2026 14:06:29 EST
        acb_info :      0x00000210
        bad_password_count:     0x00000000

[+] RID: 0x1f5]
        User Name   :   Guest
        Description :   Built-in account for guest access to the computer/domain
        Logon Time               :      Wed, 31 Dec 1969 19:00:00 EST
        acb_info :      0x00000215

[+] RID: 0x1f6]
        User Name   :   krbtgt
        Description :   Key Distribution Center Service Account
...
[+] RID: 0x487]
        User Name   :   vhayes
        Full Name   :
        Home Drive  :
        Dir Drive   :
        Profile Path:
        Logon Script:   FLAG3{3e6d07c2f9b4a158d023e7c80469ba512f93d6e2c47b081a953f10827e5}
        Description :   DISABLED — former employee, kept for audit trail
        Workstations:
        Comment     :
        Remote Dial :
        Logon Time               :      Wed, 31 Dec 1969 19:00:00 EST
        Logoff Time              :      Wed, 31 Dec 1969 19:00:00 EST
        Kickoff Time             :      Wed, 13 Sep 30828 22:48:05 EDT
        Password last set Time   :      Thu, 23 Apr 2026 07:53:12 EDT
        acb_info :      0x00000211

```
