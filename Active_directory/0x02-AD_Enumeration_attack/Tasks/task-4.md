
4. DCSync Attack

Description:

DCSync is a technique that abuses Active Directory replication rights. Instead of running code on the Domain Controller, an attacker impersonates a Domain Controller and requests password hashes directly from the real DC using the legitimate replication protocol.

    During your user enumeration, you noticed something interesting in one of the service account descriptions. 
    A backup service account appears to have unusual privileges on the domain. 
    These privileges, if abused, allow an attacker to extract every password hash in the domain  including the Administrator and krbtgt accounts.
    

This tells you svc_backup has special replication privileges on the domain

Objective:

Obtain the NTLM hash of the domain Administrator account and use it to authenticate to the Domain Controller without knowing the plaintext password.

Hints:

Hint 1 : Where to start:

Look back at your enumeration output. One service account description tells you exactly what rights it has. That account is your entry point.

Hint 2 : Getting credentials:

You already know how to extract credentials from accounts that have SPNs configured. That technique applies here too.

**Hint 3 **: Abusing the rights:

Once you have valid credentials for the privileged account, research what tool allows you to replicate domain secrets remotely. Think about what a Domain Controller does when it syncs with another DC.

Hint 4 : Using the hash:

After running the replication attack, you will obtain the Administrator NTLM hash from the output. NTLM authentication accepts this hash directly to authenticate without needing the Administrator plaintext password.

This is called Pass-the-Hash.

The flag is stored in a location that only the domain Administrator can access. Once you authenticate as Administrator, you will know where to look.

Tools: impacket-secretsdump, smbclient --pw-nt-hash, crackmapexec
