Introduction

This project-based module takes you deep into the offensive reconnaissance phase of an Active Directory engagement. Building on the foundational knowledge of Windows Server and Domain Controller architecture, you will now learn how to systematically enumerate AD environments extracting users, groups, computers, trusts, policies, and permissions and leverage that information to identify and exploit credential-based vulnerabilities. From abusing Kerberos pre-authentication weaknesses to performing DCSync attacks, you will experience the full attack chain that real-world red teamers execute during internal penetration tests. Using industry-standard tools such as impacket, BloodHound, ldapsearch, and hashcat, you will move beyond passive observation and actively abuse misconfigurations to recover credentials, escalate privileges, and read sensitive data hidden within AD attributes.
Why It Matters

Enumeration is where every successful Active Directory attack begins. Before an attacker can escalate privileges or move laterally, they must first understand the domain's structure who has what permissions, which accounts are misconfigured, and where the weakest links are. Techniques like AS-REP Roasting, Kerberoasting, and DCSync are not theoretical they appear in real breach reports, ransomware post-mortems, and red team assessments every single day. As a security professional, understanding how attackers enumerate and abuse credentials in AD environments is essential to building meaningful defenses, detecting intrusions early, and conducting thorough penetration tests that reflect the actual threat landscape.
Resources
Read or watch:

    Active Directory Objects
    Active Directory Security Deep-dive
    Red Teaming Active Directory
    Active Directory Enumeration
    Kerberos, DNS, LDAP, MSRPC
    NTLM Authentication

Requirements

    You need To Finish Active Directory - Fundamentals Before Diving in Here

Needed ISOS:

    Windows Server 2019
    Windows 11 Enterprise
    Kali Linux

Credentials used:

Username : student Password: Str0ngPass!2026

Note:

Download only the provided OVA files for Windows 11 and Windows Server. Do not modify any settings. Import them as-is.

Connect all three VMs to the same network so they can communicate: Kali Linux, Windows 11, and Windows Server.

All attack work will be done from Kali Linux targeting Windows Server. The Windows 11 VM acts as the victim workstation.
Needed Tools

    Impacket
    Impacket secretsdump.py
    Impacket secretsdump.py
    Responder
    hashcat
    Metasploit Msfconsole

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    Grasp why AD enumeration is crucial for both administrators and attackers.
    Acquire skills in using various tools and methods to extract information from AD, such as LDAP queries, built-in Windows commands, PowerShell scripts, and third-party tools.
    Recognize how information gathered through enumeration can be used to strengthen security or exploit weaknesses.
    Develop the ability to enumerate users, groups, computers, domain controllers, trusts, policies, and permissions within AD.
    Understand how to interpret the data obtained from these enumeration activities.
    Learn to identify potential security vulnerabilities and misconfigurations within AD environments.
    Enhance your ability to detect suspicious activities and potential attacks on AD environments through enumeration data.

General

    Allowed editors: vi, vim, emacs
    All your files should end with a new line.

“Students should only download and set up the Windows Server 2019 VM. All access to the environment must be performed from Kali Linux, where they are expected to obtain the Windows Server credentials through enumeration and exploitation rather than being provided directly.”
