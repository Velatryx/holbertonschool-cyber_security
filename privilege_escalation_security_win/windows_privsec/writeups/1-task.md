
## Windows PrivEsc, task 1:

---

## Our objective is given in the /windows_privsec/tasks/1-task.md

---

> First, let's download the privcheck powerhsell script, and move it to pwd: ([Download Link](https://github.com/itm4n/PrivescCheck/releases/latest/download/PrivescCheck.ps1))

> Run an extended privcheck

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended -Report PrivescCheck_$($env:COMPUTERNAME) -Format TXT,HTML"
```

> The extended check will save the output as .txt and .html. You can download the html and open it in the new tab to analyze it further [here](1-task.html)


