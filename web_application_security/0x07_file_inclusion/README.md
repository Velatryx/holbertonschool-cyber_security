Resources
Read or watch

    Local File Inclusion (LFI) – OWASP
    Remote File Inclusion (RFI) – OWASP
    LFI to RCE: Basic Exploitation Guide
    File Inclusion Types, Examples, and Prevention
    File Inclusion Path Traversal

References

    PHP Manual on include() and require()
    File Inclusion Cheat Sheet
    File Inclusion Payload Github

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What is LFI?
    What is RFI?
    How to prevent FI attacks?
    What is ../../ used for in FI?
    How can LFI lead to RCE?
    What are the mechanisms through which file inclusion vulnerabilities can be exploited?
    What is the potential impact of successful file inclusion attacks on a system?
    What techniques can be used to detect file inclusion vulnerabilities in web applications?
    How can effective mitigation strategies be implemented to safeguard against file inclusion vulnerabilities?

Requirements
General

    Allowed editors: vi, vim, emacs.
    All your scripts will be tested on Kali Linux.
    All your scripts should be exactly one line long ($ wc -l file should print 1)
    All your files should end with a new line (Why?)
    A README.md file, at the root of the folder of the project, is mandatory
    For this project, your focus will be on the target Cyber - WebSec 0x07.

Tasks
0. File Hub

Your initial objective entails identifying the vulnerable endpoint and securing the flag located at /etc/0-flag.txt.

    Target Machine: Cyber - WebSec 0x07
    Main Endpoint: http://web0x07.hbtn/task0/list_file

Useful instructions:
1. Try to upload a file.
2. Check page source for evey endpoint.
3. Investigate links and how they are processed, and what parameters are accepted.
4. Experiment with altering the path and file names and check the result.

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: web_application_security/0x07_file_inclusion
    File: 0-flag.txt

