

For this project, we expect you to look at these concepts:

    Active Directory Hardening

Introduction

This project-based module introduces you to PowerView, one of the most powerful PowerShell-based reconnaissance tools used in Active Directory engagements. Rather than relying on graphical interfaces, you will query the domain directly from the command line enumerating users, groups, GPOs, ACLs, trusts, and shares with precision and speed. Alongside enumeration, this module covers the defensive side of the equation: hardening Domain Controllers, enforcing security policies through GPOs, deploying Windows LAPS for local administrator password management, and configuring auditing to detect the very techniques you are learning to use. This dual perspective attacker enumeration with PowerView, defender hardening with GPOs and LAPS gives you a complete picture of how misconfigurations are found and how they are fixed.
Why It Matters

PowerView is not just a red team tool it is a lens through which you can see exactly what an attacker sees when they land inside your network. Security teams that understand PowerView enumeration can proactively audit their own environments, identify over-permissioned accounts, exposed ACLs, and weak GPO configurations before an adversary does. Combined with LAPS, proper auditing, and least-privilege models, the skills in this module directly map to how mature enterprise security teams protect their Active Directory infrastructure against real-world intrusions.
Resources
Read or watch:

    PowerView
    Active Directory documentation
    Group Policy Overview
    Best Practices for Securing Active Directory From Microsoft
    Active Directory Security Best Practices
    Active Directory Hardening Best Practices
    Active Directory hardening checklist & (actionable) best practices
    Securing Domain Controllers Against Attack
    How to detect, enable and disable SMBv1, SMBv2, and SMBv3 in Windows
    Configure rules with group policy
    AppLocker
    Best practices for secure administrative workstation
    Implementing Secure Administrative Hosts
    Implementing Least-Privilege Administrative Models
    What is Windows LAPS?
    Key concepts in Windows LAPS
    Get started with Windows LAPS for Windows Server Active Directory
    Configure policy settings for Windows LAPS

Requirements
Needed ISOS:

    Windows Server 2019
    Windows 11 credentials: Username: bh_intern / Password: User@2025!
    Windows 11 Enterprise
    Kali Linux

Note:

Download only the provided OVA files for Windows 11 and Windows Server. Do not modify any settings. Import them as-is.

Connect all three VMs to the same network so they can communicate: Kali Linux, Windows 11, and Windows Server.

All attack work will be done from Kali Linux targeting Windows Server. The Windows 11 VM acts as the victim workstation.

PowerView is already installed on the Windows 11 VM use it to enumerate the Active Directory environment. No installation needed.

The students will work on the Windows 11 VM to find the flags using PowerView. First, they need to bypass the PowerShell execution policy with:

Set-ExecutionPolicy Bypass -Scope Process

Then, they can load PowerView using:

. .\PowerView.ps1
Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    Understand what PowerView is and how it leverages PowerShell to query Active Directory via LDAP.
    Enumerate domain users, groups, computers, and Domain Controllers using PowerView cmdlets.
    Identify misconfigured ACLs and dangerous permissions (GenericAll, WriteDACL, GenericWrite) on AD objects.
    Enumerate Group Policy Objects and extract security-relevant configurations from them.
    Discover local admin access across domain machines using PowerView.
    Map trust relationships between domains and forests to identify lateral movement opportunities.
    Identify Kerberoastable and AS-REP Roastable accounts through PowerView enumeration.
    Chain PowerView enumeration results with credential attacks to achieve privilege escalation.

“Students will use a Windows 11 VM as their attack machine, where PowerView tools are already installed, to perform Active Directory enumeration and attacks against the target environment.”
