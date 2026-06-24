
### Our first mission is: Identify disabled domain user accounts via LDAP bitmask filtering

Blueprint:
`ldapsearch -x -H ldap://[1. Target IP] -D "[2. Bind DN]" -w '[3. Password]' -b "[4. Base DN]" "([5. UAC Bitmask Filter])" [6. Requested Attributes]`

Command:

```bash
ldapsearch -x \
-H ldap://192.168.56.20 \
-D "bh_intern@PENTESTLAB.local" \
-w 'User@2025!' \
-b "DC=PENTESTLAB,DC=local" \
"(userAccountControl:1.2.840.113556.1.4.803:=2)" \
sAMAccountName distinguishedName

```

Explanation:

`ldapsearch`: Executes the standard OpenLDAP client utility used to query and manipulate directory information trees.

`-x`: Specifies simple authentication mechanism (plaintext bind) instead of SASL.

`-H ldap://192.168.56.20`: Explicitly sets the URI address pointing to the target Domain Controller's LDAP listener.

`-D "bh_intern@PENTESTLAB.local" -w 'User@2025!'`: Provides the authenticated bind distinguished name and password for directory authentication.

`-b "DC=PENTESTLAB,DC=local"`: Establishes the structural search base anchor at the domain root level to process all downstream organizational units.

`"(userAccountControl:1.2.840.113556.1.4.803:=2)"`: Applies the Extensible Match Rule Object Identifier (OID) `1.2.840.113556.1.4.803` (`LDAP_MATCHING_RULE_BIT_AND`). This bitmask verification checks the `userAccountControl` integer array and isolates objects where the second bit (`ACCOUNTDISABLE`, value `2`) is set to true.

`sAMAccountName distinguishedName`: Limits the structural response attributes exclusively to user logon tokens and full directory path strings to preserve scannability.

Brief Explanation:

> "Query the Active Directory directory partition using a low-privileged context to evaluate specific object account flags. Dormant accounts are frequently skipped in visual assessments or surface audits but persist actively within the raw directory store. Utilizing an explicit LDAP matching rule bitwise filter unmasks every disabled identity cluster, immediately tracking down the hidden `bh_auditor` identity inside the target `BH-Users` Organizational Unit."

---

### Our final mission is: Interrogate the target disabled account schema property flags to extract hidden variables

Blueprint:
`ldapsearch -x -H ldap://[1. Target IP] -D "[2. Bind DN]" -w '[3. Password]' -b "[4. Target Base DN]" "([5. Identity Filter])" "[6. Attribute Selection]"`

Command:

```bash
ldapsearch -x \
-H ldap://192.168.56.20 \
-D "bh_intern@PENTESTLAB.local" \
-w 'User@2025!' \
-b "DC=PENTESTLAB,DC=local" \
"(sAMAccountName=bh_auditor)" \
"*"

```

Explanation:

`ldapsearch -x`: Standardizes simple authentication routines across the connection session.

`-H ldap://192.168.56.20`: Directs the attribute mapping request to the primary Domain Controller.

`-D "bh_intern@PENTESTLAB.local" -w 'User@2025!'`: Handles authentication parameters using standard internal directory credentials.

`-b "DC=PENTESTLAB,DC=local"`: Directs the global scanning parser across the target container blocks.

`"(sAMAccountName=bh_auditor)"`: Sharpens the filter logic directly onto the unique account string assigned to the target auditor profile.

`"*"`: Explicitly demands a dump of all standard user object properties and schema strings linked to the matched record.

Brief Explanation:

> "Perform a full administrative object dump against the isolated auditor profile to extract deep metadata configurations. When identities undergo deprovisioning routines, legacy environment variables, administrative keys, or structural flags are routinely abandoned inside auxiliary data categories. Scanning down the resulting attribute rows completely exposes the target operational payload hidden inside the `otherTelephone` metadata schema value."

Interaction Workflow & Retrieval:

```text
# Morgan Liu, BH-Users, BH-Project, PENTESTLAB.local
dn: CN=Morgan Liu,OU=BH-Users,OU=BH-Project,DC=PENTESTLAB,DC=local
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Morgan Liu
sn: Liu
title: IT Auditor
...
otherTelephone: BHFLAG4{D1S4BL3D_M0RG4N_L1U_F4}
userAccountControl: 66050
sAMAccountName: bh_auditor
...
# search result
search: 2
result: 0 Success

```
