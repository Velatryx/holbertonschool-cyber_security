
5. Full Attack Chain → DCSync → Golden Ticket

Description:

BloodHound maps a full privilege escalation path to Domain Admin. The chain runs through an ACL misconfiguration on a helpdesk account, a password reset on a sysadmin, and finally DCSync rights that allow dumping every hash in the domain. Objective:

    Spray → compromise bh_helpdesk
    Abuse GenericAll → reset bh_sysadmin password
    Enumerate bh_sysadmin.homePhone → FLAG BH-F5
    DCSync → dump Administrator+ krbtgt NTLM hashes
    Forge a Golden Ticket and authenticate to the DC

Tools: bloodyAD smbclient (sudo apt install smbclient -y)
