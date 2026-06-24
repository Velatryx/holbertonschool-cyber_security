
5. Kerberoasting & SPN Enumeration

Kerberoasting is one of the most well-known attacks against Active Directory environments and is extremely common in real penetration tests. It abuses the way Kerberos authentication works when service accounts are involved.

In Active Directory, service accounts are often configured with a Service Principal Name (SPN). An SPN is a unique identifier that associates a service with a specific account. Any authenticated domain user can request a Kerberos service ticket for any account that has an SPN registered this is by design and cannot be disabled.

The problem is that this service ticket is encrypted with the NTLM hash of the service account password. An attacker can request this ticket, save it to disk, and attempt to crack it offline using tools like Hashcat or John the Ripper completely without triggering any lockout because no failed login attempt occurs.

-Instructions:

In this task, you will use PowerView to enumerate all accounts in the domain that have an SPNregistered. These are your Kerberoasting targets. Once you identify the vulnerable account, capture its Kerberos ticket using PowerView and save the hash to a file. Then read a hidden attribute on that account to retrieve the flag.

Hint:

PowerView has a dedicated function to find SPN accounts and another to directly capture Kerberoastable hashes in Hashcat format. Look carefully at all attributes of the target account not just the standard ones.
