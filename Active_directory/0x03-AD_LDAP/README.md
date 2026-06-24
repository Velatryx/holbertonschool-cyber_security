Introduction

Active Directory acts as the central nervous system for enterprise networks, making it a primary target for attackers seeking total control. This project moves beyond individual host security to explore domain-wide compromise. You will analyze the structure of domains and forests, then exploit inherent trust in protocols like Kerberos and NTLM. By mastering techniques such as Kerberoasting, Pass-the-Hash, and Golden Ticket attacks, you will understand how a single weak configuration can lead to full infrastructure dominance.
Context

During an internal penetration test of a corporate network, the focus shifts from individual servers to the directory services that bind them. The target environment relies heavily on Active Directory for authentication and access control. Your mission is to map the domain structure, enumerate Service Principal Names, and identify weaknesses in authentication protocols. By chaining common misconfigurations with exploits likeKerber
Resources
Read or watch:

    LLMNR Poisoning and How to Prevent It
    Active Directory Exploitation Cheat Sheet
    Exploiting Microsoft’s Active Directory
    Active Directory Attack Methods
    Using Hashcat Tool for Microsoft Active Directory

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    How can you identify attack surfaces in Active Directory (AD)?
    How does Kerberos authentication work in Active Directory, and what techniques are used for Kerberoasting, Golden Ticket attacks, and Pass-the-Hash (PtH) attacks?
    What are the exploitation techniques that target NTLM authentication vulnerabilities and weaknesses?
    How is Active Directory (AD) structured, including domains, forests, domain controllers, and trust relationships?
    What are Service Principal Names (SPNs), and what role do they play in Windows environments?

Requirements

Needed ISOS:

    Windows Server 2019
    Windows 11 Enterprise
    Kali Linux
    The Previous Lab you Setup in Active Directory - Fundamentals

Note: You must create two virtual machines in the same network one will be a user machine and the other will be the domain controller
General

    Allowed editors: vi, vim, emacs
    All your files should end with a new line.
    Keep screenshots of every step along with the commands used.
    Ensure that all tasks are performed within the Kali Linux environment for consistency.

Needed Tools

    ldapsearch
    crackmapexec

NB: “Students should only download and set up the Windows Server 2019 VM. All access to the environment must be performed from Kali Linux, where they are expected to obtain the Windows Server credentials through enumeration and exploitation rather than being provided directly.”
