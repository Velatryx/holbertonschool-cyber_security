Introduction

This project-based module dives into the architecture and inner workings of Active Directory (AD) environments, with a focus on understanding how Windows Server and Domain Controllers are structured, and how attackers leverage misconfigurations in Users, Groups, and Group Policy Objects (GPOs) to gain footholds, escalate privileges, and move laterally across enterprise networks. You will explore real-world AD environments, analyze trust relationships, abuse permission misconfigurations, and think like an adversary operating inside a corporate domain.
Why It Matters

Active Directory is the backbone of identity and access management in over 90% of enterprise environments worldwide which makes it the single most targeted infrastructure component in modern cyberattacks. From ransomware operators to nation-state threat actors, adversaries consistently target AD to escalate privileges, establish persistence, and compromise entire organizations in a matter of hours. Understanding how Domain Controllers are configured, how Users and Groups inherit permissions, and how GPOs can be weaponized is not optional for a Red Teamer it is the foundation of every serious internal engagement. Whether you are conducting a penetration test, a red team operation, or an assumed-breach simulation, the ability to enumerate, abuse, and exploit Active Directory structures is what separates a surface-level tester from an operator who can truly simulate an advanced threat.
Resources
Read or watch:

    What is Active Directory and how does it work?
    What is an Active Directory Domain?
    What are the Benefits of Using Active Directory?
    Active Directory Prerequisites.
    how to create test users, group and organizational uni?
    Active Directory (Structure, Terminology)

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What is Active Directory?
    What is Authorization?
    What is Authentication?
    What is Domain Controllers?
    What is Domains?
    What is LDAP?

Requirements

Needed ISOS:

    Windows Server 2019
    Windows 11 Enterprise

“To connect to the Windows VM, please use WinRM from Kali Linux with the following credentials: username labuser and password P@ssw0rd123!.”

Note:

Download only the provided OVA files for Windows 11 and Windows Server. Do not modify any settings. Import them as-is.

Connect all three VMs to the same network so they can communicate: Kali Linux, Windows 11, and Windows Server.

All attack work will be done from Kali Linux targeting Windows Server. The Windows 11 VM acts as the victim workstation.
General

    Allowed editors: vi, vim, emacs
    All your files should end with a new line.

“Students should only download and set up the Windows Server 2019 VM. All access to the environment must be performed from Kali Linux, where they are expected to obtain the Windows Server credentials through enumeration and exploitation rather than being provided directly.”
Tasks
0. Domain Reconnaissance: Extracting Core Domain Information from Active Directory

Objective

Every Active Directory environment exposes fundamental information through its root domain object. Your goal is to enumerate the domain and enumerate domain attributes. A flag has been hidden inside a non-standard attribute of the domain object.

Your mission

    Query the Active Directory domain object
    Inspect both standard and non-standard attributes
    Identify the attribute containing the hidden flag

Hint: Standard domain queries do not return all available attributes. Some fields require explicit property requests to be visible.

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: Active_directory/0x01-AD_Basics_And_Concepts
    File: 0-flag.txt

