Introduction

Privilege escalation is a crucial phase during any security assessment. During this phase, we attempt to gain access to additional users, hosts, and resources to move closer to the assessment’s overall goal. There are many ways to escalate privileges. This module focuses on the most common and impactful methods seen in real client environments, emphasizing practical misconfigurations and flaws rather than rare CTF edge cases.
Module Summary

This module covers a wide variety of techniques used to escalate privileges on Linux systems. Privilege escalation is an essential skill in penetration testing and red team operations. A deep understanding of the Linux operating system, strong enumeration skills, and mastery of local privilege escalation techniques can significantly impact the success of an assessment. In this module, you will learn:

    Enumerating a Linux system effectively
    Kernel exploits
    Exploiting vulnerable services
    Abusing misconfigurations and weak permissions
    Hunting for credentials
    Shared object hijacking and library manipulation
    Leveraging privileged group memberships
    Context-dependent privilege escalation techniques
    Linux security hardening best practices

This module is broken down into clear sections with hands-on exercises to practice each technique. It concludes with a practical skills assessment to validate your understanding.

The module is classified as "Easy" but assumes a working knowledge of the Linux command line and an understanding of information security fundamentals.

PdPNCL5.webp
Resources
Read or watch:

    Linux Privilege Escalation by g0tmi1k
    GTFOBins
    SUID Exploitation Guide
    The Linux Command Line Book
    MITRE ATT&CK - Privilege Escalation
    LinPEAS on GitHub
    LinEnum on GitHub
    Linux Exploit Suggester on GitHub
    John the Ripper Website
    Metasploit Framework

Learning Objectives

At the end of this overview, you are expected to be able to explain to anyone, without the help of Google:

    Kernel Exploits: Understanding how outdated kernels are exploited using tools like dirtycow.
    SUID/SGID Executables: Identifying misconfigured executables and exploiting them with gtfobins.
    Exploiting Weak File Permissions: Finding and exploiting world-writable files to escalate privileges.
    Cron Jobs and Scheduled Tasks: Exploiting misconfigured cron jobs running with elevated privileges.
    Path Variable Manipulation: Understanding insecure PATH manipulation to gain higher privileges.
    Password Hashes and Credential Reuse: Cracking or reusing password hashes with tools like John the Ripper.
    Exploiting Services Running as Root: Identifying and exploiting vulnerable root services.
    Escaping Restricted Shells: Bypassing restricted shells using Python, GTFOBins, and other techniques.
    LDPRELOAD and LDLIBRARY_PATH Exploits: Manipulating environment variables to load malicious libraries.
    Privilege Escalation through Misconfigured sudo: Exploiting sudo configurations to execute commands as root.

Working with Commands:

    Use ps and kill commands to identify and terminate malicious processes.
    Use netstat and ss commands to monitor network traffic for suspicious activity.
    Use nmap, lynis, and tcpdump commands to analyze network traffic for suspicious behavior.
    Use iptables and ufw to manage firewall rules on Linux systems.

Requirements
General

    Allowed tools:LinPEAS, GTFOBins, Nmap, ExploitDB.
    All scripts must be tested on a Linux distribution (e.g., Ubuntu, Kali).
    Documentation for each privilege escalation technique must be included in a README.md file.
    Ensure all scripts are executable and have the correct permissions set.
    You must use descriptive comments in your code to explain the purpose of each command and technique used.
    Make sure to follow ethical guidelines and have permission to test on any target systems.
    All scripts must be checked for security best practices before execution, particularly regarding user input.
    Ensure detailed output is provided for each privilege escalation method tested, with results saved in a results.md file.
    You are not allowed to use hardcoded credentials; instead, utilize secure methods to handle credentials.

Note:

    When the file contains CTF{privilege_escalation_via_sudo_choom_579eea17d42c385d4be6a0750c6b5562}, the actual flag to submit is only the hash inside: 579eea17d42c385d4be6a0750c6b5562

To connect use:

    ssh user@ YOUR _ CONTAINER _ IP
    password : user
