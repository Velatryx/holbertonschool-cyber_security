
3. RPC User Enumeration: Enumerating Active Directory via RPC Protocol

Objective: Active Directory can be queried through multiple protocols. While LDAP is the most common, the RPC protocol exposes user and group information through a completely different interface rpcclient. Some attributes accessible via RPC are not returned by standard LDAP queries.

Your mission:

    Connect to the Domain Controller using rpcclient
    Enumerate domain users using RPC-specific commands
    Query individual user details to find the hidden flag

Tool:rpcclient

Hint: Once connected, explore commands like enumdomusers to list users and queryuser to inspect individual accounts. Pay attention to all fields returned especially for accounts that appear disabled or inactive.

Flag location: A user field returned by rpcclient queryuser not visible in standard LDAP queries.
