
2. Group Membership & Share Access

In Active Directory environments, access to resources is often controlled through group membership. A user account alone may have no special privileges, but if that account belongs to a specific group, it may gain access to sensitive network shares, applications, or systems.

A restricted SMB share exists on the Domain Controller that contains a flag. This share is not accessible to everyone only members of a specific domain group can read it. Your job is to enumerate all domain groups, identify which one grants access to this share, find out which accounts are members of that group, and then use those credentials to mount the share and read the flag.

-Instructions:

Remember that PowerShell's Get-Content cmdlet does not support the -Credential parameter on network paths. You will need to find another way to mount the share with specific credentials before reading the file.

Hint:

PowerView can list all groups in the domain and enumerate their members. Once you identify the right account, think about how to authenticate as that user to access a network resource.
