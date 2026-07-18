
```shell
Get-ChildItem -Path .\Documents\PowerShell -Recurse -Filter *.txt | ForEach-Object {
    $File = $_
    $ParentDir = Split-Path $File.Directory -Leaf
    Select-String -Path $File.FullName -Pattern "FLAG\{","flag","password","whoami /priv","net localgroup" | ForEach-Object {
        "[Folder: $ParentDir] -> Line $($_.LineNumber): $($_.Line.Trim())"
    }
}
```

I found the attacker used the password: Stud1337Password@123 to login to SuperAdministrator. So I used it too.

db9837d92367ebc82c71a2b87c16016c 
