
3. AS-REP Roasting : jmartin

Description:

A developer requested that Kerberos pre-authentication be disabled on their account for legacy application compatibility. This is a critical misconfiguration it allows any unauthenticated attacker to request an encrypted AS-REP and crack it offline.

Objective:

    Without any valid credentials, identify accounts with DoesNotRequirePreAuth set
    Capture and crack the AS-REP hash
    Authenticate as jmartinand retrieve the flag fromemployeeType
