Resources
Read or watch:

    Permissions
    Linux permissions
    Finding Files With SUID and SGID
    How to Use SUID and SGID on Linux
    Understanding Linux Special permissions
    What Is Umask and How to Use it Effectively

man or help:

    chmod
    sudo
    su
    chown
    chgrp
    id
    groups
    adduser
    useradd
    addgroup

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What are the three user-based permission groups in Linux
    What are the Linux commands chmod, sudo, su, chown, and chgrp used for
    What is the purpose of the setuid and setgid in Linux file permissions, and how do you use them
    What is the difference between the chown and chgrp commands
    What are some best practices for managing file permissions on Linux
    How can you audit file permissions changes on your system
    What is Umask in Linux

General

    Allowed editors: vi, vim, emacs.
    All your scripts will be tested on Kali Linux.
    You must substitute the IP range for $1.
    All your files should end with a new line (Why?)
    The first line of all your files should be exactly #!/bin/bash.
    A README.md file, at the root of the folder of the project, is mandatory
    You are not allowed to use backticks, && or ||.
    Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
    All your files must be executable

Tasks
0. Who can add a new user in Linux!

Write a bash script that generates a new user and sets a password for that specific user.

    Your script should accept a username as an arguments $1.
    Your script should accept a password as an arguments $2.
    File lines length = 3
    Not allowed to use printf

Depending on your machine, the output could change.

┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo ./0-add_user.sh holberton H@ck$@f3Gu@rD!
[sudo] password for maroua:
New password: Retype new password: passwd: password updated successfully
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 tail -1 /etc/passwd
holberton:x:1005:1005::/home/holberton:/bin/sh
┌──(maroua㉿HBTN-LAB)-[~/Permissions, SUID & SGID]
└─🏴 sudo tail -1 /etc/shadow
[sudo] password for maroua:
holberton:$y$j9T$hX9xRbjAKGGXawAjjRbay.$byRISNEKNJeoUr5s8K4.QNDU5HgV2oocPJ6qYyBbHm0:19669:0:99999:7:::
