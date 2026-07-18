
1. Privilege Escalation via SAM & SYSTEM Backup Files
Objective

Your objective is to exploit a vulnerability in the system to recover the superAdministrator password and retrieve the flag.
Your target machine is Virtual Machine (VM): LAB02

    The password for the Sammy account is :

Sammy
Steps to Complete

    Privilege Enumeration

    Download and run the PrivCheck PowerShell script on the target system.
    Analyze the output to identify the vulnerability .

    Research and Exploitation

    Research the vulnerability online.
    Locate and download a working vulnerability file .exe exploit.
    Use the exploit to extract critical files from the target system.

    Hash Extraction

    Switch to Kali Linux and ensure the Impacket toolkit is installed.
    Use the secretdump.py tool to extract hashed password from the files.

    Administrator Session Access

    Use the recovered hashes to open an Administrator session.
    Obtain the flag from the session and save it.
