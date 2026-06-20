Description:

Any authenticated domain user can request a Kerberos service ticket (TGS) for any account that has a Service Principal Name (SPN) registered. The ticket is encrypted using the service account's password hash which means it can be taken offline and cracked without triggering any account lockout.

Your mission:

    Enumerate all accounts with SPNs registered in the domain
    Request their TGS tickets as an authenticated user
    Crack the ticket hash offline to recover the plaintext password
    Use the cracked credentials to access a protected SMB share

Tools: impacket-GetUserSPNs, hashcat, smbclient

Hint:

    Service accounts often have weak passwords. The share is only accessible with the correct cracked credentials.
    The name of the protected share reflects the attack technique used to access it.

Flag location: Inside a restricted SMB share accessible only with the cracked service account password.
