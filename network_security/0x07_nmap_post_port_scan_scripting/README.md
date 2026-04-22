Resources
Read or watch:
Nmap documentation
Nmap Scripting Engine
Tips Nmap Script Engine
Advanced Port Scanning techniques
Nmap Scripts (NSE): The Key To Enhance Your Network Scans
Nmap Scripting
List of NMAP Scripts
References:
Nmap Scripting Engine
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

What is the Nmap Scripting Engine (NSE) and why is it important?
How does the Nmap Scripting Engine work?
What are the different script categories in NSE?
How are scripts organized and executed in NSE?
What command-line arguments are used for running NSE scripts?
What can you do with these Nmap scripts?
How do you write documentation for NSE scripts using NSEDoc?
Requirements
General
Allowed editors: vi, vim, emacs.
All your scripts will be tested on Kali Linux.
All your scripts should be exactly two lines long ($ wc -l file should print 2)
You must substitute the IP range for $1.
All your files should end with a new line (Why?)
The first line of all your files should be exactly #!/bin/bash.
A README.md file, at the root of the folder of the project, is mandatory
You are not allowed to use backticks, &&, || or ;.
All your scripts should be 2 lines long ($ wc -l file should print = 2).
You are not Allowed to use Neither echo
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
All your files must be executable
Ensure that $1 is used without quotes in your script to prevent unintended argument type alterations.
warning
Don't use " or ' surrounding $1.
You have to refer to ports by their numbers instead of their service names.
Tasks
0. Skipping NSE scripting for Nmap is like bringing a spoon to a hacking knife fight!


You might be familiar with the robust open-source network scanning tool Nmap, but have you heard about the even more potent Nmap Scripting Engine?

The Nmap Scripting Engine NSE is an advanced feature of the open-source network scanning tool Nmap . It automates network scanning and exploitation tasks, saving time and enhancing capabilities through scripting.

We have observed that many security professionals lack the ability to write NSE scripts for Nmap. This skill is relatively easy to learn, and by neglecting it, you are leaving a lot of value on the table. Let's dive in and learn everything we need to become experts in the Nmap Scripting Engine today!

Write a bash script that runs the default NSE scripts using default to perform various analyses and gather necessary information related to the target.

Your script should accept a host as an arguments $1
Depending on the scanned network, the output could change.

┌──(maroua)-[~/0x07_nmap_post_port_scan_scripting]
└─🏴 sudo ./0-nmap_default.sh scanme.nmap.org
[sudo] password for maroua:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-06-24 13:00 CET
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.19s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
| ssh-hostkey: 
|   1024 ac:00:a0:1a:82:ff:cc:55:99:dc:67:2b:34:97:6b:75 (DSA)
|   2048 20:3d:2d:44:62:2a:b0:5a:9d:b5:b3:05:14:c2:a6:b2 (RSA)
|   256 96:02:bb:5e:57:54:1c:4e:45:2f:56:4c:4a:24:b2:57 (ECDSA)
|_  256 33:fa:91:0f:e0:e1:7b:1f:6d:05:a2:b0:f1:54:41:56 (ED25519)
80/tcp    open  http
|_http-title: Go ahead and ScanMe!
9929/tcp  open  nping-echo
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 16.19 seconds
Repo:

GitHub repository: holbertonschool-cyber_security
Directory: network_security/0x07_nmap_post_port_scan_scripting
File: 0-nmap_default.sh
