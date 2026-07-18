
## Windows PrivEsc, task 1:

---

## Our objective is given in the /windows_privsec/tasks/1-task.md

---

> First, let's download the privcheck powerhsell script, and move it to pwd: ([Download Link](https://github.com/itm4n/PrivescCheck/releases/latest/download/PrivescCheck.ps1)

> Run a basic privcheck

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
```

> Output:

```
PS C:\Users\Sammy> powershell -ep bypass -c ". .\PrivescCheck.ps1;Invoke-PrivescCheck"
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ CATEGORY
┃ TA0043 - Reconnaissance
┃
┃ NAME
┃ User - Identity
┃
┃ TYPE
┃ Base
┃
┣━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ Get information about the current user(name,domain name)┃
┃ and its access token(SID,integrity level,authentication ┃
┃ ID).
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
Name : DESKTOP-4V9TPK3\Sammy
SID : S-1-5-21-3687015499-3071869482-3054830844-1000 IntegrityLevel : Medium Mandatory Level(S-1-16-8192)
SessionId : 1 TokenId : 00000000-0029d938 AuthenticationId : 00000000-000b4b93 OriginId : 00000000-000003e7 ModifiedId : 00000000-000b4bdf Source : User32(00000000-000b4b03)[*] Status: Informational - Severity: None - Execution time: 00:00:00.460 ┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ CATEGORY
┃ TA0043 - Reconnaissance
┃
┃ NAME
┃ User - Groups
┃
┃ TYPE
┃ Base
┃
┣━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ Get information about the groups the current user belongs to
┃
┃(name,type,SID).
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
Name Type SID ---- ---- ---
DESKTOP-4V9TPK3\None
Group
S-1-5-21-3687015499-3071869482-3054830844-513
Everyone WellKnownGroup S-1-1-0 BUILTIN\Users
Alias S-1-5-32-545 NT AUTHORITY\INTERACTIVE WellKnownGroup S-1-5-4 CONSOLE LOGON WellKnownGroup S-1-2-1 NT AUTHORITY\Authenticated Users WellKnownGroup S-1-5-11 NT AUTHORITY\This Organization WellKnownGroup S-1-5-15 NT AUTHORITY\Local account WellKnownGroup S-1-5-113 NT AUTHORITY\LogonSessionId_0_739993 LogonSession S-1-5-5-0-739993 LOCAL WellKnownGroup S-1-2-0 NT AUTHORITY\NTLM Authentication WellKnownGroup S-1-5-64-10 Mandatory Label\Medium Mandatory Level Label S-1-16-8192
[*] Status: Informational - Severity: None - Execution time: 00:00:00.247
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ CATEGORY
┃ TA0004 - Privilege Escalation
┃
┃ NAME
┃ User - Privileges
┃
┃ TYPE
┃ Base
┃
┣━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ Check whether the current user is granted privileges that
┃
┃ can be leveraged for local privilege escalation.
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
Name State Description Exploitable ---- ----- ----------- -----------
SeShutdownPrivilege Disabled
Shut down the system False
SeChangeNotifyPrivilege Enabled
Bypass traverse checking False
SeUndockPrivilege Disabled
Remove computer from docking station False
SeIncreaseWorkingSetPrivilege Disabled
Increase a process working set False
SeTimeZonePrivilege Disabled
Change the time zone False
[*] Status: Informational(not vulnerable)- Severity: None - Execution time: 00:00:00.146
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ CATEGORY ┃ TA0004 - Privilege Escalation
┃
┃ NAME
┃ User - Privileges(GPO)
┃
┃ TYPE
┃ Base
┃
┣━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ Check whether the current user is granted privileges,
┃
┃ through a group policy,that can be leveraged for local
┃
┃ privilege escalation.
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
[*] Status: Informational(not vulnerable)- Severity: None - Execution time: 00:00:00.376
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ CATEGORY ┃ TA0006 - Credential Access ┃ ┃ NAME ┃ User - Environment Variables ┃ ┃ TYPE ┃ Base ┃ ┣━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ┃ Check whether any environment variables contain sensitive ┃ ┃ information such as credentials or secrets. Note that this ┃ ┃ check follows a keyword-based approach and thus might not be ┃ ┃ completely reliable. ┃ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ [*] Status: Informational(nothing found)- Severity: None - Execution time: 00:00:00.163 ┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ┃ CATEGORY ┃ TA0004 - Privilege Escalation ┃ ┃ NAME ┃ Services - Non-Default Services ┃ ┃ TYPE ┃ Base ┃ ┣━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ┃ Get information about third-party services. It does so by ┃ ┃ parsing the target executable's metadata and checking ┃ ┃ whether the publisher is Microsoft. ┃ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ Name : GoogleChromeElevationService DisplayName : Google Chrome Elevation Service(GoogleChromeElevationService)ImagePath : "C:\Program Files\Google\Chrome\Application\133.0.6943.59\elevation_service.exe" User : LocalSystem StartMode : Manual UserCanStart : False UserCanStop : False Name : GoogleUpdaterInternalService152.0.7933.0 DisplayName : Google Updater Internal Service(GoogleUpdaterInternalService152.0.7933.0)ImagePath : "C:\Program Files(x86)\Google\GoogleUpdater\152.0.7933.0\updater.exe" --system --windows-service --service=update-internal User : LocalSystem StartMode : Automatic UserCanStart : False UserCanStop : False Name : GoogleUpdaterService152.0.7933.0 DisplayName : Google Updater Service(GoogleUpdaterService152.0.7933.0)ImagePath : "C:\Program Files(x86)\Google\GoogleUpdater\152.0.7933.0\updater.exe" --system --windows-service --service=update User : LocalSystem StartMode : Automatic UserCanStart : False UserCanStop : False Name : ssh-agent DisplayName : OpenSSH Authentication Agent ImagePath : C:\Windows\System32\OpenSSH\ssh-agent.exe User : LocalSystem StartMode : Disabled UserCanStart : True UserCanStop : False Name : VGAuthService DisplayName : VMware Alias Manager and Ticket Service ImagePath : "C:\Program Files\VMware\VMware Tools\VMware VGAuth\VGAuthService.exe" User : LocalSystem StartMode : Automatic UserCanStart : False UserCanStop : False Name : vm3dservice DisplayName : @oem8.inf,%VM3DSERVICE_DISPLAYNAME%;VMware SVGA Helper Service ImagePath : C:\Windows\system32\vm3dservice.exe User : LocalSystem StartMode : Automatic UserCanStart : False UserCanStop : False Name : VMTools DisplayName : VMware Tools ImagePath : "C:\Program Files\VMware\VMware Tools\vmtoolsd.exe" User : LocalSystem StartMode : Automatic UserCanStart : False UserCanStop : False [*] Status: Informational - Severity: None - Execution time: 00:00:04.169 ┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ┃ CATEGORY ┃ TA0004 - Privilege Escalation ┃ ┃ NAME ┃ Services - Known Vulnerable Kernel Drivers ┃ ┃ TYPE ┃ Base ┃ ┣━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ┃ Check whether known vulnerable kernel drivers are installed. ┃ ┃ It does so by computing the file hash of each driver and ┃ ┃ comparing the value against the list provided by ┃ ┃ loldrivers.io. ┃ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ [*] Status: Informational(not vulnerable)- Severity: None - Execution time: 00:01:14.373 ┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ┃ CATEGORY ┃ TA0004 - Privilege Escalation ┃ ┃ NAME ┃ Services - Permissions ┃ ┃ TYPE ┃ Base ┃ ┣━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ┃ Check whether the current user has any write permissions on ┃ ┃ a service through the Service Control Manager(SCM). ┃ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ PS C:\Users\Sammy>

```
