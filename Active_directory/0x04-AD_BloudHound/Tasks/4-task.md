

Description:

Disabled accounts are frequently overlooked in security audits. BloodHound renders them differently in the graph, but they still exist in LDAP and can hold sensitive data. Hunt down the disabled auditor account and extract its hidden flag.

Objective:

    Query LDAP for all disabled accounts using the userAccountControl bitmask filter
    Identify bh_auditor in the BH-Users OU
    Enumerate all its attributes and retrieve the flag from otherTelephone
