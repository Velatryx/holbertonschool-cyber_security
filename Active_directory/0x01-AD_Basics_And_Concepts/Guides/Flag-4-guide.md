Markdown

# 4. Hidden User Attribute Discovery: Finding Sensitive Data in Overlooked User Properties

This technical writeup details the methodology for auditing Active Directory user objects to discover non-standard configuration properties, data leakages, and credentials hidden within extended directory attributes.

---

### 🎯 Objective & Mission Parameters

Active Directory user objects contain dozens of distinct attributes, many of which are never populated during standard corporate deployments. Because administrative tools like Active Directory Users and Computers (`dsa.msc`) suppress empty or operational fields by default, administrators occasionally use them to store temporary deployment notes, setup scripts, or legacy passwords.

* **Task:** Enumerate domain security accounts and extract non-standard user properties.
* **Target:** Isolate an account featuring an anomalous operational profile or flag signature.
* **Repository Target:** `holbertonschool-cyber_security/Active_directory/0x01-AD_Basics_And_Concepts/4-flag.txt`

> [!TIP]
> Standard LDAP directory sweeps only return a default set of primitive structural attributes. To audit for hidden fields or administrative comments, your search query must explicitly compel the Domain Controller to return complete attribute arrays (via `-Properties *` in PowerShell or `* +` flags in `ldapsearch`).

---

## 🔍 Stage 1: Broad Directory Auditing via Remote PowerShell

Using the active administrative token generated within our interactive Windows Remote Management (`evil-winrm`) session, we leverage the native `Get-ADUser` cmdlet to run an omnibus query across the entire domain partition.

By passing the wildcard `-Filter *` alongside an explicit requests array `-Properties *`, we bypass standard console visibility filters and dump all metadata strings directly into a formatted list pipeline.

```powershell
Get-ADUser -Filter * -Properties * | Select-Object SamAccountName, Title, Description, Info, Comment, adminDescription | Format-List
```
Alternative Lower-Level Evaluation (ADSI Engine)

If environmental constraints or execution policies restrict structural module compilation, the same data vector can be evaluated utilizing the raw .NET Active Directory Service Interfaces (ADSI) search engine wrapper:
PowerShell
```
$S = [adsisearcher]"(&(objectCategory=person)(objectClass=user))"
$S.PropertiesToLoad.AddRange(@('samaccountname','title','description','info','comment','admindescription'))
$S.FindAll() | ForEach-Object { $_.Properties }
```
⚡ Stage 2: Parsing Extended Attributes & Asset Isolation

The domain database returns a comprehensive property array containing all registered network user profiles. While scanning through standard service profiles and infrastructure accounts, a highly explicit anomaly is discovered within the structural description fields:
High-Value Targets Directory Extraction Log
Plaintext
```
SamAccountName   : jadmin
Title            : IT Administrator
Description      : IT Administrator - Domain Admin

SamAccountName   : legacy
Title            : 
Description      : Legacy account - no kerberos preauth
Comment          : FLAG_M2_T0{fe952761a0d5d62e32caa49d4a72e57e8765def3e720d3f5600fd7285d4a}

SamAccountName   : carol.white
Title            : HR Manager
Description      : FLAG4{ab312724162e30809801f7c0490f547317ba8cf3fbc243819264ddf0e52b}
Info             : 
Comment          : 
adminDescription :

SamAccountName   : svc.backup
Title            : Service
Description      : FLAG1{747fb213581c9cd487fc6e77bf4e54aa6321839fe023b0551ceef706cbc6}
```
The account matched to SamAccountName: carol.white carries a highly non-standard Description attribute value containing the explicit assignment for this tracking milestone.
📊 Stage 3: Property Breakdown Analysis

The following directory matrix maps the specific structural paths verified during this auditing phase:
Targeted Field	Assigned Value	Asset Classification
Object DN	CN=Carol White,OU=Lab_Users,DC=PENTESTLAB,DC=local	Active Directory Leaf Object
sAMAccountName	carol.white	Security Identifier Handle
title	HR Manager	Functional Identity Context
description	FLAG4{ab312724162e30809801f7c0490f547317ba8cf3fbc243819264ddf0e52b}	Insecure Metadata Exposure
🧠 Offensive Security Post-Mortem

    The Exposure: A production domain account (carol.white) had a sensitive high-value validation asset string written directly to its global directory Description field attribute.

    The Vulnerability Principle: Free-text organizational properties (such as description, info, comment, or postalAddress) are frequently treated by IT departments as private text fields. Because these entries are primarily intended for identity reporting and are hidden from normal Windows client interactions, administrators mistake lack of default visibility for authentic security boundaries.

    The Escalation Path: Active Directory security descriptors grant all standard authenticated domain participants (NT AUTHORITY\Authenticated Users) structural read permissions across common user schema items. As a result, any internal user, low-privileged automation agent, or compromised workstation can programmatically scrape the entire directory database to locate high-value flags or hardcoded credentials without generating access violation alerts.

    [!IMPORTANT]
    Captured Mission Flag:

    FLAG4{ab312724162e30809801f7c0490f547317ba8cf3fbc243819264ddf0e52b}
