Markdown

# 3. Registry Investigation: Discovering Hidden Data in the Windows Registry

This technical writeup details the methodology for enumerating the Windows Registry architecture via a remote administrative session to discover custom configuration containers and exposed sensitive data.

---

## 🎯 Objective & Mission Parameters

Not all critical data or configuration mistakes reside within Active Directory directory objects. Systems administrators frequently utilize the local machine's registry hives to store custom software flags, hardcoded configurations, application metadata, or legacy system variables.

* **Task:** Navigate the local Windows registry hives to isolate non-standard keys.
* **Target:** Identify custom subkeys that do not conform to native Windows baseline software structures.
* **Repository Target:** `holbertonschool-cyber_security/Active_directory/0x01-AD_Basics_And_Concepts/3-flag.txt`

> [!TIP]
> Focus your post-exploitation structural review inside the `SOFTWARE` configuration subtree within the Local Machine hive (`HKEY_LOCAL_MACHINE`). Look closely for organizational or environment-specific naming schemes.

---

## 🚧 Stage 1: Establishing the Remote WinRM Command Session

During the preceding Active Directory group discovery phase, we corrected a credential syntax issue and validated that the account `labuser` with the password `P@ssw0rd123!` was explicitly provisioned within high-privilege groups. This grants the token interactive execution rights via Windows Remote Management (WinRM).

Using the offensive shell toolkit `evil-winrm`, we initiate an authenticated session targeting the Domain Controller endpoint (`192.168.56.20`).

```bash
evil-winrm -i 192.168.56.20 -u labuser -p 'P@ssw0rd123!'

Terminal Event Log
Plaintext

Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline                                         
Data: For more information, check Evil-WinRM GitHub: [https://github.com/Hackplayers/evil-winrm#Remote-path-completion](https://github.com/Hackplayers/evil-winrm#Remote-path-completion)                                         
Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\labuser\Documents>

Why Did This Succeed?

    Valid Domain Token: The credential string alignment (P@ssw0rd123!) matches the domain database constraints.

    Remote Management Rights: Because labuser is verified as an active member of administrative containers, Windows access control lists allow the generation of a remote interactive execution thread (wsmprovhost.exe).

🔍 Stage 2: Enumerating the Local Machine Software Hive

The Windows Registry is organized into distinct logical structures called hives. The HKEY_LOCAL_MACHINE\SOFTWARE (HKLM:\SOFTWARE) path contains configuration profiles for all applications installed on the system, making it a primary target for finding insecure third-party deployments.

From our active PowerShell prompt, we execute a structural directory listing command against the HKLM:\SOFTWARE path to map out every registered subkey.
PowerShell

Get-ChildItem -Path HKLM:\SOFTWARE

Extracted Core Registry Hive Output
Plaintext

    Hive: HKEY_LOCAL_MACHINE\SOFTWARE

Name                    Property
----                    --------
Classes
Clients
DefaultUserEnvironment  Path : C:\Users\labuser\AppData\Local\Microsoft\WindowsApps;
                        TEMP : C:\Users\labuser\AppData\Local\Temp
                        TMP  : C:\Users\labuser\AppData\Local\Temp
Google
HolbertonLab            TaskFlag : FLAG3{921d2a56bd128240587aa7abbcad0a37fb8e5c6e091fa763754f27648fbe}
Intel
Microsoft
Mozilla
ODBC
OpenSSH
Oracle
Partner
Policies
RegisteredApplications  File Explorer             : SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Capabilities
                        Paint                     : SOFTWARE\Microsoft\Windows\CurrentVersion\Applets\Paint\Capabilities
Setup
WOW6432Node

⚡ Stage 3: Targeted Data Extraction & Key Verification

The structural mapping command reveals a custom key container (HolbertonLab) that is not part of a default Windows installation baseline. PowerShell automatically displays top-level object properties inline, exposing the targeted string asset entry.

To cleanly isolate and verify this configuration item explicitly, we query the absolute path using the Get-ItemProperty cmdlet.
PowerShell

Get-ItemProperty -Path HKLM:\SOFTWARE\HolbertonLab

Parameter Breakdown
Command component	Purpose
Get-ItemProperty	Retrieves the explicit property values associated with a designated path.
-Path	Specifies the targeted registry drive location string.
HKLM:\SOFTWARE\HolbertonLab	The complete path to the verified non-standard software key node.
Property Dump Output
Plaintext

TaskFlag     : FLAG3{921d2a56bd128240587aa7abbcad0a37fb8e5c6e091fa763754f27648fbe}
PSPath       : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\HolbertonLab
PSParentPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE
PSChildName  : HolbertonLab
PSDrive      : HKLM
PSProvider   : Microsoft.PowerShell.Core\Registry

📊 Stage 4: Extracted Key Properties & Analysis

The data structure breakdown verifies that the parameter values match the required flag pattern.
Plaintext

HolbertonLab            TaskFlag : FLAG3{921d2a56bd128240587aa7abbcad0a37fb8e5c6e091fa763754f27648fbe}

🧠 Offensive Security Post-Mortem

    The Exposure: A custom software node named HolbertonLab was written directly under the machine's global software configuration directory tree, holding an unencrypted high-value token asset string inside a registry value named TaskFlag.

    The Vulnerability Principle: Developers and administrators often utilize registry hives as a quick storage solution for scripts, setup logs, or operational environment keys. They treat the registry as an opaque database under the assumption that an attacker will not actively scan non-standard software hives.

    The Escalation Path: Because the HKEY_LOCAL_MACHINE\SOFTWARE container has default read access permissions granted to standard system users and domain members authenticated to the endpoint, any configuration values kept here without custom Access Control Lists (ACLs) are instantly exposed to internal recon tools or low-privilege enumeration scripts.

    [!IMPORTANT]
    Captured Mission Flag:

    FLAG3{921d2a56bd128240587aa7abbcad0a37fb8e5c6e091fa763754f27648fbe}3. Registry Investigation: Discovering Hidden Data in the Windows Registry

This technical writeup details the methodology for enumerating the Windows Registry architecture via a remote administrative session to discover custom configuration containers and exposed sensitive data.
🎯 Objective & Mission Parameters

Not all critical data or configuration mistakes reside within Active Directory directory objects. Systems administrators frequently utilize the local machine's registry hives to store custom software flags, hardcoded configurations, application metadata, or legacy system variables.

    Task: Navigate the local Windows registry hives to isolate non-standard keys.

    Target: Identify custom subkeys that do not conform to native Windows baseline software structures.

    Repository Target: holbertonschool-cyber_security/Active_directory/0x01-AD_Basics_And_Concepts/3-flag.txt

    [!TIP]
    Focus your post-exploitation structural review inside the SOFTWARE configuration subtree within the Local Machine hive (HKEY_LOCAL_MACHINE). Look closely for organizational or environment-specific naming schemes.

⚡ Stage 1: Establishing the Remote WinRM Command Session

During the preceding Active Directory group discovery phase, we corrected a credential syntax issue and validated that the account labuser with the password P@ssw0rd123! was explicitly provisioned within high-privilege groups. This grants the token interactive execution rights via Windows Remote Management (WinRM).

Using the offensive shell toolkit evil-winrm, we initiate an authenticated session targeting the Domain Controller endpoint (192.168.56.20).
Bash

evil-winrm -i 192.168.56.20 -u labuser -p 'P@ssw0rd123!'

Session Initialization Log
Plaintext

Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline                                         
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                         
Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\labuser\Documents>

The console successfully binds to the remote host management engine, returning an active PowerShell execution instance.
🔍 Stage 2: Enumerating the Local Machine Software Hive

The Windows Registry is organized into distinct logical structures called hives. The HKEY_LOCAL_MACHINE\SOFTWARE (HKLM:\SOFTWARE) path contains configuration profiles for all applications installed on the system, making it a primary target for finding insecure third-party deployments.

From our active PowerShell prompt, we execute a structural directory listing command against the HKLM:\SOFTWARE path to map out every registered subkey.
PowerShell

Get-ChildItem -Path HKLM:\SOFTWARE

Extracted Core Registry Hive Output
Plaintext

    Hive: HKEY_LOCAL_MACHINE\SOFTWARE

Name                    Property
----                    --------
Classes
Clients
DefaultUserEnvironment  Path : C:\Users\labuser\AppData\Local\Microsoft\WindowsApps;
                        TEMP : C:\Users\labuser\AppData\Local\Temp
                        TMP  : C:\Users\labuser\AppData\Local\Temp
Google
HolbertonLab            TaskFlag : FLAG3{921d2a56bd128240587aa7abbcad0a37fb8e5c6e091fa763754f27648fbe}
Intel
Microsoft
Mozilla
ODBC
OpenSSH
Oracle
Partner
Policies
RegisteredApplications  File Explorer             : SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Capabilities
                        Paint                     : SOFTWARE\Microsoft\Windows\CurrentVersion\Applets\Paint\Capabilities
                        Windows Address Book      : Software\Clients\Contacts\Address Book\Capabilities
                        Windows Disc Image Burner : Software\Microsoft\IsoBurn\Capabilities
Setup
WOW6432Node

📊 Stage 3: Data Extraction & Key Verification

The output from our structural mapping command reveals a custom key container that is not part of a default Windows installation baseline:  
Plaintext

HolbertonLab            TaskFlag : FLAG3{921d2a56bd128240587aa7abbcad0a37fb8e5c6e091fa763754f27648fbe}

PowerShell automatically displays top-level object properties inline. To cleanly extract this single configuration item, we query the absolute path using the Get-ItemProperty cmdlet:
PowerShell

Get-ItemProperty -Path HKLM:\SOFTWARE\HolbertonLab

Property Dump Output
Plaintext

TaskFlag     : FLAG3{921d2a56bd128240587aa7abbcad0a37fb8e5c6e091fa763754f27648fbe}
PSPath       : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\HolbertonLab
PSParentPath : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE
PSChildName  : HolbertonLab
PSDrive      : HKLM
PSProvider   : Microsoft.PowerShell.Core\Registry

The value stored inside the custom TaskFlag string matches the target criteria for this deployment phase.
🧠 Offensive Security Post-Mortem

    The Exposure: A custom software node named HolbertonLab was written directly under the machine's global software configuration directory tree, holding an unencrypted high-value token asset string inside a registry value named TaskFlag.

    The Vulnerability Principle: Developers and administrators often utilize registry hives as a quick storage solution for scripts, setup logs, or operational environment keys. They treat the registry as an opaque database under the assumption that an attacker will not actively scan non-standard software hives.

    The Escalation Path: Because the HKEY_LOCAL_MACHINE\SOFTWARE container has default read access permissions granted to standard system users and domain members authenticated to the endpoint, any configuration values kept here without custom Access Control Lists (ACLs) are instantly exposed to internal recon tools or low-privilege enumeration scripts.

    [!IMPORTANT]
    Captured Mission Flag:
    FLAG3{921d2a56bd128240587aa7abbcad0a37fb8e5c6e091fa763754f27648fbe}
