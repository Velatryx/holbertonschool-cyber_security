

For this project, we expect you to look at these concepts:

    Network File System (NFS)
    Simple Mail Transfer Protocol (SMTP)
    Simple Network Management Protocol (SNMP)

Resources
Read or watch:

    Network Protocols Explained (TCP/IP, UDP, ICMP, DNS, DHCP)
    What is SMTP? - Simple Mail Transfer Protocol Explained
    SNMP Explained: Network Monitoring Protocol Made Easy
    SMB Protocol Explained: File Sharing Between Devices
    Understanding LDAP: Lightweight Directory Access Protocol
    Remote Desktop Protocol (RDP) Explained
    The Network Stack & Protocols Explained
    Cybersecurity Protocols: Understanding HTTPS, SFTP, SSH
    Understanding Network Protocols: A Beginner's Guide
    Network Protocols Explained: A Comprehensive Guide

References:

    List of Network Protocols
    Glossary of Cyber Security Terms
    HackerOne Blog - Network Security Resources

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What is the purpose of the NSF protocol?
    How does SMTP work to send emails?
    What information does SNMP provide about network devices?
    How does SMB enable file sharing between different operating systems?
    What is the role of LDAP in authentication and authorization?
    Explain the security risks associated with using RDP.
    Differentiate between secure protocols like HTTPS and SFTP from their insecure counterparts.
    Explain the benefits of using SSH for secure remote access.
    Explain the concept of port numbers and their significance in network communication.
    Differentiate between different types of network encryption protocols.
    Explain the importance of keeping network protocols up-to-date and patched.

Requirements
General

    All your files will be run on Kali Linux 2023.2
    Allowed editors: vi, vim, emacs
    You must substitute the IP range for $1.
    The first line of all your files should be exactly #!/bin/bash.
    All your files should end with a new line.
    All your scripts should be 2 lines long $ wc -l file should print 2.
    Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl

Tasks
0. Analyze iptables Rules

Write a script to display all current iptables rules in a readable format, including line numbers.

$ sudo ./0-iptables.sh
Chain DOCKER-USER (1 references)
num   pkts bytes target     prot opt in     out     source               destination         
1        0     0 RETURN     0    --  *      *       0.0.0.0/0            0.0.0.0/0 

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: linux_security/0x03_protocols_servers
    File: 0-iptables.sh

