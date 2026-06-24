
2. Kerberoasting : svc_backup

Description:

BloodHound reveals a service account exposing a Veeam Backup SPN. Service accounts often have weak passwords set years ago and never rotated. Crack it and enumerate the account.

Objective:

    Enumerate all Kerberoastable accounts in the domain
    Request the TGS ticket and crack it offline
    Authenticate as svc_backup and retrieve the flag from its homeDirectory attribute
