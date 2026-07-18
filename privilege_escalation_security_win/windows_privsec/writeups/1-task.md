
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


