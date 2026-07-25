Introduction

Gaining initial access to a system is often fleeting; persistence makes it permanent. In the lifecycle of a cyber attack, maintaining a foothold is critical for long-term engagement, allowing attackers to survive reboots, retain control, and stage further operations. This project delves into the art of Windows Persistence, exploring how adversaries embed themselves deep within the operating system. You will manipulate benign system features—such as the Startup folder, Registry keys, and WMI subscriptions to turn a compromised machine into a permanent asset, understanding that true control means ensuring access never ends.
Context

You have successfully compromised a Windows workstation within a target network. However, your current foothold is fragile; a system restart or a user logoff could sever your connection instantly. Your mission is to establish robust persistence mechanisms that survive reboots and maintain access regardless of user activity. Using the provided environment, you will transition from temporary access to permanent residency, testing various techniques from simple Startup folder modifications to complex WMI event subscriptions. You must document the efficacy and stealth of each method, ensuring that once you are in, you stay in.
Resources
Read or Watch:

    MITRE ATT&CK - Persistence
    Windows Internals Book
    The Art of Memory Forensics
    Windows Red Team Persistence Techniques
    What is the Startup Folder?
    Introduction to the Windows Startup Folder
    How to Clean an Infected Computer
    Autoruns for Windows

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What Windows persistence is and why it’s important in cybersecurity.
    The different techniques used to establish persistence on a Windows system.
    How to utilize the Startup folder, registry keys, and scheduled tasks for persistence.
    The risks associated with DLL hijacking and how to mitigate them.
    How to leverage WMI for executing malicious code based on system events.
    The significance of using BITS jobs for downloading malicious payloads.

Requirements
General

    Allowed tools: Metasploit, PowerShell, Cobalt Strike.
    All scripts should be tested in ….. (vm)
    Documentation for each persistence technique must be included in a README.md file.
    Ensure all scripts are executable and compatible with the target operating system.
    You must use descriptive comments in your code to explain each step of the process.
    All files related to your project should be organized in a dedicated project directory.
    Make sure to follow ethical guidelines and have permission to test on any target systems.-
    All scripts must be checked for security best practices before execution.
    Ensure you provide detailed output for each persistence method tested, saving results in a results.md file.
    You are not allowed to use hardcoded credentials; utilize environment variables or secure storage methods instead.

Virtual Machine (VM): VM

The password for the student account is : Student

The password for the SuperAdministrator account is : Root@123


> DISCLAIMER:

[ ! WARNING ]
This repository is maintained strictly for ethical hacking education, defensive engineering research, and authorized red-team lab testing. Executing persistence mechanisms or unauthorized command chains against production systems without explicit, prior written legal consent is strictly illegal.
