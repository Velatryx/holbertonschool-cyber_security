
### 0. AS-REP Roasting

Description:

In Active Directory, Kerberos pre-authentication is enabled by default and requires a user to prove their identity before receiving a ticket. However, some accounts have this protection disabled meaning anyone can request an encrypted AS-REP ticket for that account without knowing the password. This ticket can then be cracked offline using a wordlist attack.

Your mission:

  Enumerate all domain accounts and identify which ones have pre-authentication disabled
  Request their AS-REP hashes from the Domain Controller
  Crack the hash offline using a wordlist attack to recover the plaintext password
  Use the recovered credentials to authenticate and read a hidden LDAP attribute not visible through standard enumeration tools

Tools: `impacket-GetNPUsers`, `hashcat`, `ldapsearch`

Hints:

    During enumeration you noticed a user account described as having no kerberos preauth that is your target
    Not all LDAP attributes are visible through CME or standard tools the flag lives in the comment attribute
    Rockyou wordlist is enough to crack the hash

Flag location: comment attribute of the vulnerable account only readable after successful authentication with cracked credentials.
