
1. Service Account Enumeration: Investigating Misconfigured Service Account Attributes

Objective:

Service accounts are often poorly maintained. Sensitive information is sometimes stored directly in user attributes visible to any authenticated domain user. Your goal is to find what has been left behind.

Your mission:

Focus on service accounts (accounts with prefixes like svc) Focus on service accounts and inspect their attributes carefully Look beyond standard properties

Hint: The flag is stored in an attribute that is not shown by default enumeration. You need to explicitly request extended properties to retrieve it

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: Active_directory/0x01-AD_Basics_And_Concepts
    File: 1-flag.txt



