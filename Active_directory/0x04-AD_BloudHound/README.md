Introduction

This project-based module places you in the role of a red team operator conducting a structured attack path analysis against a live Active Directory environment. Using BloodHound as your primary weapon, you will collect, visualize, and exploit the relationships between users, groups, computers, and ACLs within the pentestlab.local domain. From your initial onboarding credentials as a low-privileged intern, you will progressively chain together misconfigurations abusing GenericAll ACLs, performing Kerberoasting and AS-REP Roasting, extracting secrets via DCSync, forging Golden Tickets, and leaking sensitive data through SYSVOL/SMB until full domain compromise is achieved. This module combines forensic log analysis with offensive tooling, bridging the gap between understanding how attacks unfold and how defenders detect them through Windows Event IDs, PowerShell logging, and Group Policy auditing.
Why It Matters

BloodHound fundamentally changed how red teamers and defenders think about Active Directory security. What was once a manual, time-consuming process of tracing permission chains across hundreds of objects became a graph-based analysis that exposes the shortest path to Domain Admin in seconds. In real engagements, attack chains like the ones you will execute here from a low-privileged user account all the way to a Golden Ticket are not edge cases. They are the norm in poorly hardened enterprise environments. Understanding how to map these paths, exploit ACL abuses, and chain credential attacks together is a critical competency for any red teamer, and equally essential for the blue teamer trying to detect and break those same paths before an adversary does.
Resources
Read or watch:
Built-in Windows Tools:

    How to Use Event Viewer
    PowerShell Documentation
    Group Policy Management Console Guide
    Greater Visibility Through PowerShell Logging
    How To Timeline Login Information From Windows Event Logs

Third-Party Tools:

    BloodHound GitHub
    ADRecon GitHub
    Mimikatz GitHub
    Sysinternals Suite

Learning Resources:

    Active Directory Forensics
    Kerberoasting Explained

Needed ISOS :
Needed ISOS:

    Windows Server 2019
    Windows 11 Enterprise
    Installing BloodHound

Notes:

Download only the provided OVA files for Windows 11 and Windows Server. Do not modify any settings. Import them as-is.

Connect all three VMs to the same network so they can communicate: Kali Linux, Windows 11, and Windows Server.

All attack work will be done from Kali Linux targeting Windows Server. The Windows 11 VM acts as the victim workstation.
Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    Understand how BloodHound collects and visualizes Active Directory relationships to reveal attack paths.
    Enumerate AD objects, LDAP attributes, and ACL permissions using BloodHound and complementary tools.
    Identify and exploit misconfigured Access Control Lists (ACLs) such as GenericAll privileges.
    Perform credential-based attacks including Kerberoasting, AS-REP Roasting, and Password Spraying.
    Execute a DCSync attack to extract domain credential hashes and understand its forensic indicators.
    Forge a Golden Ticket using extracted Kerberos secrets and understand the persistence it provides.
    Detect sensitive data leakage through SYSVOL and SMB share enumeration.
    Recognize and analyze Windows Event IDs associated with each stage of the attack chain.
    Chain multiple misconfigurations together to achieve full domain compromise from a low-privileged account.
    Document and report attack paths and findings in a clear, structured manner.

“Students should only download and set up the Windows Server 2019 VM. All access to the environment must be performed from Kali Linux, where they are expected to obtain the Windows Server credentials through enumeration and exploitation rather than being provided directly.”
