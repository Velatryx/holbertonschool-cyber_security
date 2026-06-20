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


