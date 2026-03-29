Resources
Read or watch:

    Insecure direct object references (IDOR)
    All About Insecure Direct Object Reference(IDOR)
    Insecure Direct Object Reference (IDOR) Explained
    IDOR ? Ok but what is it finally ?
    OWASP TOP 10: Insecure Direct Object Reference
    Insecure Direct Object Reference (IDOR) - A Deep Dive
    Everything You Need to Know About IDOR
    Types of IDOR
    How to find more IDORs
    IDOR Mitigation Best Practices

References:

    IDOR
    Testing for IDOR
    Cheat Sheet

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What is an IDOR?
    What does insecure direct object reference mean?
    How IDOR works?
    What is the difference between IDOR and other vulnerabilities?
    How an IDOR Attack Happens?
    What are the types of IDOR?
    What is the impact of IDOR?
    How to detect IDOR vulnerabilities?
    How to prevent IDOR attacks?
    What are the IDOR Mitigation Best Practices?

Requirements
General

    Allowed editors: vi, vim, emacs.
    All your scripts will be tested on Kali Linux.
    All your scripts should be exactly one line long ($ wc -l file should print 1)
    All your files should end with a new line (Why?)
    A README.md file, at the root of the folder of the project, is mandatory
    For this project, your focus will be on the target Cyber - WebSec 0x06.

Tasks
0. Uncovering User IDs
Navigating the IDOR Waters through A Banking Adventure 🏦!

Warmning up..

Welcome to the first step in your journey through the realm of Insecure Direct Object References (IDOR), set against the backdrop of a carefully crafted banking application.
Your mission begins with the foundational element of many IDOR vulnerabilities: discovering other users' IDs.

Understanding how user IDs are structured, assigned, and exposed can provide you with the initial foothold required to explore deeper vulnerabilities within the application.
Let's dive in.

    Target Application: CyberBank
    Initial Endpoint: http://web0x06.hbtn/dashboard

Useful instructions:
1. Log into CyberBank using provided credentials and start exploring features, paying close attention to any mention or use of user IDs.
2. Observe the URL structure, page content, and any API requests for patterns in how user IDs are displayed or transmitted.
3. Investigate other areas of the application where user-specific actions occur (e.g., transaction history, settings) for additional exposure of user IDs.
4. Experiment with altering user ID values in URLs or requests to access information pertaining to other users.
5. Within the info of a target user, identify and note down a unique flag as proof of successfully uncovering user IDs.
