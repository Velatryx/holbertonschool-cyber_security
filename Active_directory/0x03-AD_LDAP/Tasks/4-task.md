
4. Advanced LDAP Filtering on AS-REP Targets: Targeting Vulnerable Accounts with Custom LDAP Filters

Objective:

Standard LDAP queries return all users. Advanced LDAP filtering lets you target specific account configurations such as accounts with Kerberos pre-authentication disabled. These accounts are AS-REP Roasting targets. One such account has a flag hidden in an extended attribute that only appears when querying with a precise filter.

Your mission:

    Build an LDAP filter to identify accounts with pre-authentication disabled
    Query those specific accounts for all available attributes
    Find the flag stored in an extended attribute

Tool: ldapsearch with advanced LDAP filters

Hint: The LDAP filter for accounts without pre-auth uses userAccountControl bit flags. Once you identify the target account, request all attributes explicitly the flag is in an extensionAttribute field.

Flag location: An extensionAttribute field on the AS-REP Roasting target account.
