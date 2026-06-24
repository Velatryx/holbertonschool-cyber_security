
1. Password Spray + GenericAll ACL Discovery

Description:

BloodHound graph analysis reveals that an IT Support account holds unusual ACL rights over a privileged user. You need to first compromise this account via password spray, then enumerate its profile.

Objective:

    Extract the domain user list
    Perform a password spray using the default company password policy
    Authenticate as the discovered account and enumerate its LDAP attributes
    Retrieve the flag from a telephone field
