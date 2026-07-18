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
