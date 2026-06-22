

0. Basic LDAP Enumeration: Discovering Exposed User Attributes via Unauthenticated LDAP

Objective:

Some Domain Controllers allow partial LDAP queries without authentication. Your first task is to perform an anonymous LDAP enumeration and extract information from user attributes that are exposed without credentials.

Your mission:

    Attempt an anonymous LDAP bind against the Domain Controller
    Enumerate user objects in the domain
    Look for attributes that reveal sensitive or hidden data

Tool: ldapsearch without -D and -w flags

Hint: Start without credentials. Some attributes on user objects are readable anonymously. Focus on users in the LDAP-Project OU and check non-standard fields.

Flag location: A non-standard attribute of a user object readable without authentication.
