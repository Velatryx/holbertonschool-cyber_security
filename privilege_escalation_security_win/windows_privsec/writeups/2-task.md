## Windows PrivEsc, Task 2

---

> As mentioned in the task, there is a service which runs with elevated privileges, which loads a dll from a writable directory. We need to hijack that dll and escalate our privileges.
.
> The repo we are going to use is https://github.com/ShiroiBoushi/Privesc-Flipper-Zero/tree/main. We need to download "WIN10RpcClient.exe" from here.


---

## PrivCheck: PrivEsc trajectory enumeration:

> Download the privcheck ps script from [here](https://github.com/itm4n/PrivescCheck/releases/latest/download/PrivescCheck.ps1)

> Then use it with extended checks, and generate a report:

```shell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended -Report PrivescCheck_$($env:COMPUTERNAME) -Format TXT,HTML"
```

> Output: [here](2-task.html)

![image](https://github.com/Velatryx/holbertonschool-cyber_security/blob/main/privilege_escalation_security_win/windows_privsec/Images/Screenshot%20From%202026-07-18%2020-20-40.png)


> Looks like we have 2 High, and 2 moderate severity vulnerabilities that can be exploited to escalate our privileges. Download the .html file and browse it on your browser for further analysis.

First Vulnerability: (Write Permissions)

```
Services - Image File Permissions
Check whether the current user has any write permissions on a service's binary or its folder.

High


Name              : Confluence190824093953
DisplayName       : Atlassian Confluence Confluence190824093953
User              : LocalSystem
ImagePath         : "C:\Program Files\Atlassian\Confluence\bin\tomcat9.exe" //RS//Confluence190824093953
StartMode         : Automatic
Type              : Win32OwnProcess
RegistryKey       : HKLM\SYSTEM\CurrentControlSet\Services
RegistryPath      : HKLM\SYSTEM\CurrentControlSet\Services\Confluence190824093953
Status            : Running
UserCanStart      : False
UserCanStop       : False
ModifiablePath    : C:\Program Files\Atlassian\Confluence\bin\tomcat9.exe
IdentityReference : BUILTIN\Users (S-1-5-32-545)
Permissions       : AllAccess
```


Second Vulnerability: (Ghost DLL Hijacking)

```
Configuration - PATH Folder Permissions
Check whether the current user has any write permissions on the system-wide PATH folders. If so, the system could be vulnerable to privilege escalation through ghost DLL hijacking.

High


Path              : C:\Program Files\Atlassian\Confluence\bin
ModifiablePath    : C:\Program Files\Atlassian\Confluence\bin
IdentityReference : BUILTIN\Users (S-1-5-32-545)
Permissions       : AllAccess
```

Third Vulnerability: (May not be remarkable)

```
Services - Registry Permissions (Extended)
Check whether the current user has any write permissions on the extended settings of a service in the registry. This may not necessarily result in a privilege escalation. Further analysis is required.

Medium


Name              : embeddedmode
StartMode         : Manual
ImagePath         : C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted -p
User              : LocalSystem
ModifiablePath    : HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\embeddedmode\Parameters
IdentityReference : NT AUTHORITY\Authenticated Users (S-1-5-11)
Permissions       : QueryValue, CreateSubKey, EnumerateSubKeys, Notify, ReadControl, GenericRead
Status            : Stopped
UserCanStart      : True
UserCanStop       : False

Name              : embeddedmode
StartMode         : Manual
ImagePath         : C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted -p
User              : LocalSystem
ModifiablePath    : HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\embeddedmode\Parameters
IdentityReference : NT AUTHORITY\INTERACTIVE (S-1-5-4)
Permissions       : QueryValue, CreateSubKey, EnumerateSubKeys, ReadControl
Status            : Stopped
UserCanStart      : True
UserCanStop       : False

Name              : vds
StartMode         : Manual
ImagePath         : C:\Windows\System32\vds.exe
User              : LocalSystem
ModifiablePath    : HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\vds\Alignment
IdentityReference : NT AUTHORITY\Authenticated Users (S-1-5-11)
Permissions       : QueryValue, CreateSubKey, EnumerateSubKeys, ReadControl
Status            : Stopped
UserCanStart      : False
UserCanStop       : False
```
