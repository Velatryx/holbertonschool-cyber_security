
### Our first mission is: Ingest structural Active Directory environment topology via automated graph collectors

Blueprint:
`bloodhound-python -ns [1. Nameserver IP] -d "[2. Target Domain]" -u '[3. Username]' -p '[4. Password]' -c [5. Collection Loop Types] --zip`

Command:

```bash
bloodhound-python -ns 192.168.56.20 -d "DC=PENTESTLAB,DC=local" -u 'bh_intern' -p 'User@2025!' -c All --zip

```

Explanation:

`bloodhound-python`: Executes the Python-engineered port of the SharpHound ingestor tool to map active directory object relationships out of band from a non-domain joined Linux node.

`-ns 192.168.56.20`: Directs the collector to leverage the specific Domain Controller IP address as its resolution nameserver handle for directory service queries.

`-d "DC=PENTESTLAB,DC=local"`: Targets the designated domain namespace boundary context to parse object graph edges.

`-u 'bh_intern'`: Supplies the low-privileged onboarding username allocated to initiate authenticated operations.

`-p 'User@2025!'`: Passes the cleartext credential string associated with the querying identity to satisfy the active directory bind requirement.

`-c All`: Requests the maximum investigative collection scope parameters—compiling complete tracking records for Group Memberships, Domain Trusts, Local Admin privileges, Active Sessions, and Object ACL rights.

`--zip`: Instructs the data ingestor engine to automatically package the generated JSON structure outputs into a single compressed archive payload file ready for Neo4j UI analysis.

Brief Explanation:

> "Deploy an automated BloodHound data collection loop against the corporate domain controller at 192.168.56.20 using the newly acquired onboarding intern credentials. This process maps out control tracks, group delegations, and access paths across the topology. Although importing this gathered archive package into the BloodHound graphical interface allows an analyst to track critical privilege escalation vectors, standard graph analysis setups may omit localized account property values. When target parameters are not exposed within the UI node fields, it is necessary to pivot to raw, targeted directory query tools to extract hidden profile data strings."

---

### Our next mission is: Interrogate targeted user profiles and isolate hidden object properties via NetExec LDAP queries

Blueprint:
`nxc ldap [1. Target IP] -u '[2. Username]' -p '[3. Password]' --base-dn '[4. Search Anchor]' --query "([5. Target Filter])" "[6. Attribute Filters]"`

Command:

```bash
nxc ldap 192.168.56.20 -u 'bh_intern' -p 'User@2025!' --base-dn "DC=PENTESTLAB,DC=local" --query "(sAMAccountName=bh_intern)" "*" 

```

Explanation:

`nxc ldap`: Invokes NetExec's specialized LDAP protocol engine utility to authenticate against and execute operations inside the Active Directory catalog database.

`192.168.56.20`: Declares the destination network IP address of the corporate Domain Controller listening on standard LDAP port 389.

`-u 'bh_intern'`, `-p 'User@2025!'`: Explicitly passes the low-privileged credential bundle to establish a valid authenticated directory bind session.

`--base-dn "DC=PENTESTLAB,DC=local"`: Establishes the absolute search root anchor, directing the crawl recursively down the domain partition tree.

`--query "(sAMAccountName=bh_intern)" "*"`: Executes an explicit logical search filter targeting the exact Security Accounts Manager name assigned to the session, while appending the trailing wildcard parameter to mandate a complete dump of all available standard and extended schema attribute fields.

Brief Explanation:

> "Establish an authenticated directory query mapping session using NetExec to target the explicit profile parameters bound to the intern profile object. By supplying a comprehensive wildcard selector directly to the directory lookup string, the query forces the Domain Controller to return all populated fields associated with the user record, overriding default restricted output layouts. This allows an operator to systematically audit every account attribute block, uncovering administrative flags leaked within non-standard descriptive lines or custom informational slots like the pager attribute."

Interaction Workflow & Retrieval:

```text
LDAP        192.168.56.20   389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:PENTESTLAB.local) (signing:None) (channel binding:No TLS cert) 
LDAP        192.168.56.20   389    DC01             [+] PENTESTLAB.local\bh_intern:User@2025! 
LDAP        192.168.56.20   389    DC01             [+] Response for object: CN=Blake Harper,OU=BH-Users,OU=BH-Project,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             objectClass          top
LDAP        192.168.56.20   389    DC01                                  person
LDAP        192.168.56.20   389    DC01                                  organizationalPerson
LDAP        192.168.56.20   389    DC01                                  user
LDAP        192.168.56.20   389    DC01             cn                   Blake Harper
LDAP        192.168.56.20   389    DC01             sn                   Harper
LDAP        192.168.56.20   389    DC01             title                IT Trainee
LDAP        192.168.56.20   389    DC01             description          New IT trainee — BloodHound collection entry point
LDAP        192.168.56.20   389    DC01             physicalDeliveryOfficeName BH-Floor1
LDAP        192.168.56.20   389    DC01             givenName            Blake
LDAP        192.168.56.20   389    DC01             distinguishedName    CN=Blake Harper,OU=BH-Users,OU=BH-Project,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             instanceType         4
LDAP        192.168.56.20   389    DC01             whenCreated          20260427093158.0Z
LDAP        192.168.56.20   389    DC01             whenChanged          20260624130619.0Z
LDAP        192.168.56.20   389    DC01             uSNCreated           319639
LDAP        192.168.56.20   389    DC01             memberOf             CN=BH-Lab-Users,OU=BH-Groups,OU=BH-Project,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             uSNChanged           430312
LDAP        192.168.56.20   389    DC01             department           Information Technology
LDAP        192.168.56.20   389    DC01             company              PentestLab Corp
LDAP        192.168.56.20   389    DC01             name                 Blake Harper
LDAP        192.168.56.20   389    DC01             objectGUID           500fe3ee-1dca-254f-b9a3-a675042a8b33
LDAP        192.168.56.20   389    DC01             userAccountControl   66048
LDAP        192.168.56.20   389    DC01             badPwdCount          0
LDAP        192.168.56.20   389    DC01             codePage             0
LDAP        192.168.56.20   389    DC01             countryCode          0
LDAP        192.168.56.20   389    DC01             badPasswordTime      134225363305818433
LDAP        192.168.56.20   389    DC01             lastLogoff           0
LDAP        192.168.56.20   389    DC01             lastLogon            134231562071982245
LDAP        192.168.56.20   389    DC01             pwdLastSet           134217559187251552
LDAP        192.168.56.20   389    DC01             primaryGroupID       513
LDAP        192.168.56.20   389    DC01             objectSid            S-1-5-21-281050671-1125578517-3338290938-1174
LDAP        192.168.56.20   389    DC01             accountExpires       9223372036854775807
LDAP        192.168.56.20   389    DC01             logonCount           32
LDAP        192.168.56.20   389    DC01             sAMAccountName       bh_intern
LDAP        192.168.56.20   389    DC01             sAMAccountType       805306368
LDAP        192.168.56.20   389    DC01             userPrincipalName    bh_intern@pentestlab.local
LDAP        192.168.56.20   389    DC01             objectCategory       CN=Person,CN=Schema,CN=Configuration,DC=PENTESTLAB,DC=local
LDAP        192.168.56.20   389    DC01             dSCorePropagationData 20260427093158.0Z
LDAP        192.168.56.20   389    DC01                                    16010101000000.0Z
LDAP        192.168.56.20   389    DC01             lastLogonTimestamp   134267799792645596
LDAP        192.168.56.20   389    DC01             pager                BHFLAG0{BL00DH0UND_C0LL3CT10N_ST4RT_F0}

```

---

### Our final mission is: Extract raw structural object schema parameters via Native Authenticated LDAP Interrogation

Blueprint:
`ldapsearch [1. Authentication Type] [2. Target Connection] [3. Bind Identity] [4. Search Anchor] [5. Account Filter] [6. Wildcard Selector]`

Command:

```bash
ldapsearch -x -H ldap://192.168.56.20 -D "bh_intern@PENTESTLAB.local" -b "DC=PENTESTLAB,DC=local" -w 'User@2025!' "(sAMAccountName=bh_intern)" "*"

```

Explanation:

`-x`: Specifies simple authentication mechanism to transmit credentials over direct bind handshakes without SASL layer negotiation.

`-H ldap://192.168.56.20`: Points the query execution engine to the exact uniform network identifier hosting the domain directory database.

`-D "bh_intern@PENTESTLAB.local"`: Sets the explicit User Principal Name (UPN) bind identity string utilized to authenticate the requesting connection session.

`-b "DC=PENTESTLAB,DC=local"`: Mandates the top-level Distinguished Name search anchor boundary context to trigger a vertical object tree validation traversal.

`-w 'User@2025!'`: Submits the raw string password associated with the authenticated user profile handle directly to the DC.

`"(sAMAccountName=bh_intern)"`: Applies a specific search filter logic boundary to isolate the matching employee profile object record from the broader directory partition.

`"*"`: Appends the directory wildcard flag parameter to force the Domain Controller response to explicitly list every standard structural parameter populated inside the database row.

Brief Explanation:

> "Perform a raw validation check against the active directory tree using the native `ldapsearch` utility to completely expose the underlying schema layouts of the object. While graph databases excel at charting link paths between network entities, programmatic command-line lookups provide raw verification of hidden parameters. Forcing a comprehensive structural property printout isolates extended directory entries—such as user descriptions, timestamp logs, and distinct operational fields like the `pager` attribute—recovering flag components planted inside administrative placeholders."

Interaction Workflow & Retrieval:

```text
# extended LDIF
#
# LDAPv3
# base <DC=PENTESTLAB,DC=local> with scope subtree
# filter: (sAMAccountName=bh_intern)
# requesting: * #

# Blake Harper, BH-Users, BH-Project, PENTESTLAB.local
dn: CN=Blake Harper,OU=BH-Users,OU=BH-Project,DC=PENTESTLAB,DC=local
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Blake Harper
sn: Harper
title: IT Trainee
description:: TmV3IElUIHRyYWluZWUg4oCUIEJsb29kSG91bmQgY29sbGVjdGlvbiBlbnRyeSBw
 b2ludA==
physicalDeliveryOfficeName: BH-Floor1
givenName: Blake
distinguishedName: CN=Blake Harper,OU=BH-Users,OU=BH-Project,DC=PENTESTLAB,DC=
 local
instanceType: 4
whenCreated: 20260427093158.0Z
whenChanged: 20260624130619.0Z
uSNCreated: 319639
memberOf: CN=BH-Lab-Users,OU=BH-Groups,OU=BH-Project,DC=PENTESTLAB,DC=local
uSNChanged: 430312
department: Information Technology
company: PentestLab Corp
name: Blake Harper
objectGUID:: UA/j7h3KJU+5o6Z1BCqLMw==
userAccountControl: 66048
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 134225363305818433
lastLogoff: 0
lastLogon: 134231562071982245
pwdLastSet: 134217559187251552
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAAL37AEBX3FkP6RvrGlgQAAA==
accountExpires: 9223372036854775807
logonCount: 32
sAMAccountName: bh_intern
sAMAccountType: 805306368
userPrincipalName: bh_intern@pentestlab.local
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=PENTESTLAB,DC=local
dSCorePropagationData: 20260427093158.0Z
dSCorePropagationData: 16010101000000.0Z
lastLogonTimestamp: 134267799792645596
pager: BHFLAG0{BL00DH0UND_C0LL3CT10N_ST4RT_F0}

```
