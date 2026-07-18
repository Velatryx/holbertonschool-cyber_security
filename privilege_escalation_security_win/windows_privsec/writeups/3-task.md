
```shell
Get-ChildItem -Path .\Documents\PowerShell -Recurse -Filter *.txt | ForEach-Object {
    $File = $_
    $ParentDir = Split-Path $File.Directory -Leaf
    Select-String -Path $File.FullName -Pattern "FLAG\{","flag","password","whoami /priv","net localgroup" | ForEach-Object {
        "[Folder: $ParentDir] -> Line $($_.LineNumber): $($_.Line.Trim())"
    }
}
```
