Introduction

In hardened environments, the commands you rely on are often the first ones blocked. Blacklists, restricted shells, and filtered inputs are standard defensive measures and getting past them requires more than memorizing alternative syntax.

This lesson teaches you how to think beyond the obvious. You will learn how to bypass command restrictions using techniques such as globbing, argument obfuscation, and character substitution - methods that exploit the flexibility of the shell itself rather than relying on blocked commands. You will also gain a deeper understanding of how shell filters and blacklists are implemented, which is just as valuable: knowing how defenders build these restrictions is what allows you to find the gaps they missed.

The goal is not just to memorize tricks. It is to develop the problem-solving mindset that separates a capable security professional from someone who stops at the first locked door. Whether you are a penetration tester navigating a hardened target or a security analyst auditing your own defenses, the ability to operate creatively under constraints is a skill you will use throughout your career.

    Get your hands on the terminal. The faster you get comfortable here, the faster everything else in cybersecurity will make sense.

Resources
Read or watch:

    The Linux Command Line by William Shotts
    Bash Guide for Beginners
    ShellCheck: An online shell script analysis tool
    Microsoft PowerShell Documentation
    Windows Command Line Cheat Sheet
    PowerShell.org: Articles and resources for learning PowerShell

References:

    Escaping Restricted Linux Shells

    Bash Documentation

    Bypassing Blacklisted Commands

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What is a shell and why is it important in both Linux and Windows environments?
    How do shells like Bash and PowerShell work?
    What are the basic and advanced features of Bash?
    How do you write and execute shell scripts?
    What are the key differences between CMD and PowerShell in Windows?
    How can PowerShell be used cross-platform across Linux and macOS?
    What role does the shell play in system administration and automation?

Requirements
General

    Allowed editors: vi, vim, emacs.
    All your scripts will be tested on Kali Linux.
    All your scripts should be exactly one line long ($ wc -l file should print 1).
    All your files should end with a new line.
    A README.md file, at the root of the folder of the project, is mandatory.
