
6. SYSVOLSMBLeak

Description:

As a domain user inside Pentestlab Corp, you have access to the internal network and standard user permissions. During an internal security review, you are asked to investigate whether sensitive files are exposed through shared network resources.

Your task is to inspect the SYSVOL SMBshare, which is commonly used in Active Directory environments to store logon scripts, Group Policy Objects (GPOs), and administrative files. Since SYSVOL is readable by all authenticated users, attackers often target it during reconnaissance to discover credentials, scripts, or confidential notes left by administrators.

Using your provided domain account, you must access the SYSVOL share, locate the file bh_notes.txt, and recover the hidden flag stored inside.

Objective

    Connect to the SYSVOL SMB share using the provided low-privileged domain credentials
    Enumerate accessible folders and identify sensitive files inside the share
    Retrieve the file bh_notes.txt from the scripts directory
    Extract the flag hidden inside the file

Credentials given: bh_intern / User@2025!
