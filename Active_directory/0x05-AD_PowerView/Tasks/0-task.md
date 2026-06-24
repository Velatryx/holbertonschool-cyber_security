
0. Domain Reconnaissance

Provide a brief explanation of why limiting Domain Admin accounts is critical for security. Every penetration test against an Active Directory environment starts with reconnaissance. Before attempting any attack, you need to understand the structure of the domain you are targeting.

-Instructions:

In this task, you will use PowerView to enumerate the basic properties of the domain. You are looking for the domain name, the hostname of the Domain Controller, its operating system version, and the domain functional level. These details tell you what attacks are possible and what version of Windows you are dealing with.

Active Directory stores information about the domain itself as an object in LDAP. This object has many attributes some are standard, some are custom. Administrators sometimes store sensitive information in attributes that are not displayed by default.

Your goal is to enumerate the domain object and all its attributes. The flag is hidden in one of them.

Hint:

PowerView has a function to query any AD object by its Distinguished Name and retrieve specific or all properties.
