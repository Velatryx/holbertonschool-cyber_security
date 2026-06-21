
3. LDAP / adminDescription

Description:

Active Directory stores far more information than what standard tools display by default. Attributes like adminDescription on domain objects are not returned by common enumeration commands but are fully accessible via direct LDAP queries or BloodHound collection. Attackers use these techniques to map the full AD attack surface and find hidden data.

Your mission:

Perform a direct LDAP query against the domain object Request non-standard attributes that are not shown by default enumeration tools Optionally run BloodHound to collect and visualize all AD relationships

Tools: ldapsearch

Hint:

The flag is stored in an attribute of the domain object itself not on any user or group.

Flag location:

adminDescription attribute of the Domain object readable via authenticated LDAP query.
