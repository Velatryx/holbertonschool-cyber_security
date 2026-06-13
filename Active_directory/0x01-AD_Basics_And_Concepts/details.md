┌──(root㉿kali)-[~]
└─# nmap --min-rate=1000 192.168.56.20  
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-13 13:45 -0400
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 192.168.56.20
Host is up (0.00077s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE
53/tcp   open  domain
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
5985/tcp open  wsman
MAC Address: 08:00:27:1E:B7:E4 (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 2.32 seconds


TASK 3==========================================================
┌──(root㉿kali)-[~]
└─# evil-winrm -i 192.168.56.20 -u labuser -p 'P@ssw0rd123!'
                                        
Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\labuser\Documents> Get-ChildItem -Path HKLM:\SOFTWARE


    Hive: HKEY_LOCAL_MACHINE\SOFTWARE


Name                           Property
----                           --------
Classes
Clients
DefaultUserEnvironment         Path : C:\Users\labuser\AppData\Local\Microsoft\WindowsApps;
                               TEMP : C:\Users\labuser\AppData\Local\Temp
                               TMP  : C:\Users\labuser\AppData\Local\Temp
Google
HolbertonLab                   TaskFlag : FLAG3{921d2a56bd128240587aa7abbcad0a37fb8e5c6e091fa763754f27648fbe}
Intel
Microsoft
Mozilla
ODBC
OpenSSH
Oracle
Partner
Policies
RegisteredApplications         File Explorer             : SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Capabilities
                               Paint                     : SOFTWARE\Microsoft\Windows\CurrentVersion\Applets\Paint\Capabilities
                               Windows Address Book      : Software\Clients\Contacts\Address Book\Capabilities
                               Windows Disc Image Burner : Software\Microsoft\IsoBurn\Capabilities
                               Windows Photo Viewer      : Software\Microsoft\Windows Photo Viewer\Capabilities
                               Windows Search            : Software\Microsoft\Windows Search\Capabilities
                               Wordpad                   : Software\Microsoft\Windows\CurrentVersion\Applets\Wordpad\Capabilities
                               Internet Explorer         : SOFTWARE\Microsoft\Internet Explorer\Capabilities
                               Windows Media Player      : Software\Clients\Media\Windows Media Player\Capabilities
Setup
WOW6432Node



