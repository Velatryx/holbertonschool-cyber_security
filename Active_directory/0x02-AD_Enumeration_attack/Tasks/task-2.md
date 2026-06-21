
2. LDAP Enumeration and BloodHound

Description:

Active Directory user attributes such as description are readable by any authenticated domain user including remotely over SMB. Administrators sometimes store passwords or sensitive notes in these fields for convenience, unknowingly exposing credentials to any attacker with a foothold in the domain.

Your mission:

    Enumerate all domain users and their description fields
    Identify a cleartext password stored in one of the descriptions
    Use those credentials to authenticate and access a restricted SMB share

Tools: crackmapexec, smbclient

Hint:

Read every description carefully during your enumeration. The password is hiding in plain sight.

Flag location:

Inside a restricted SMB share accessible only with the discovered credentials.

