
```shell
Get-ChildItem -Path .\Documents\PowerShell -Recurse -Filter *.txt | Select-String -Pattern "password", "whoami", "net localgroup", "SecureString"
```
