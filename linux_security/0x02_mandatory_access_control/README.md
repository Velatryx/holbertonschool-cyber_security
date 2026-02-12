Resources
Read or watch:

    Introduction to Mandatory Access Control (MAC)
    Your visual how-to guide for SELinux policy enforcement
    5 security technologies to know in Red Hat Enterprise Linux
    AppArmor: An alternative to SELinux
    Linux Security: MAC, DAC, and RBAC
    Security-Enhanced Linux for mere mortals
    AppArmor vs SELinux: What's the Difference?
    semanage Command with Examples

References:

    National Institute of Standards and Technology (NIST) on MAC
    SELinux
    SELinux Project Wiki
    AppArmor Project Wiki
    CentOS Documentation on SELinux
    Arch Linux Wiki on Security
    Linux Kernel Capabilities and MAC
    semanage

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What is MAC in Linux?
    How does SELinux enforce MAC?
    What are the differences between SELinux and AppArmor?
    What is the purpose of policy in MAC systems?
    How do labels work in SELinux?
    What are Type Enforcement, Role-Based Access Control, and Multi-Level Security in SELinux?
    How can you check the status of SELinux on a system?
    What are common SELinux management commands?
    How do you set file contexts in SELinux?
    What is an AppArmor profile?
    How do you reload AppArmor profiles?
    What is the concept of least privilege in MAC?
    How do you troubleshoot SELinux issues?
    What is the significance of audit logs in MAC systems?
    Can you explain the concept of capabilities in Linux security?
    How to use semanage

Requirements
General

    All your files will be run on Kali Linux 2023.2
    Allowed editors: vi, vim, emacs
    You must substitute the IP range for $1.
    The first line of all your files should be exactly #!/bin/bash.
    All your files should end with a new line.
    All your scripts should be 2 lines long $ wc -l file should print 2.
    Not allowed to use printf
    You are not allowed to use backticks, &&, || or ;.
    Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl

Tasks
0. Is your Linux feeling like Fort Knox or a wide-open saloon today?

SELinux modes: because even Linux needs its choose your adventure security setting. Enforcing is the hard mode, Permissive is the easy mode with cheat codes, and Disabled is the living life on the wild side option. What's your Linux's security mood today?

Write a bash script that prints the current SELinux mode on your system

Depending on your machine, the output could change.

┌──(maroua㉿HBTN-LAB)-[~/0x02_mandatory_access_control]
└─🏴 `sudo ./0-analyse_mode.sh`
[sudo] password for maroua: 
SELinux status:                 disabled

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: linux_security/0x02_mandatory_access_control
    File: 0-analyse_mode.sh

