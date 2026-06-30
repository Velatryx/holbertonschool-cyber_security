
0. Escape the Blacklist and Read the Flag

Your goal is to read the content of the file located at /home/user/flag, but with a twist—certain commands and approaches are blacklisted.

You need to find a creative way to read the flag using alternative methods to bypass the blacklist.
Restricted Commands

The following commands and patterns are blacklisted: bash, sh, zsh, SHELL, grep, vi, vim, scp, ssh, awk, tar, nano, pico, ed, ex, gedit, emacs, kate, lime, jed, find, |, -, echo, for, while, do, done, if, {}, and others.

Attempts to use any blacklisted command will result in an error.
Your goal

Find a way to read the contents of /home/user/flag.
You cannot directly reference the file's name as it appears.
target machine for this task:

    cyber shell 0x01 task2

to connect use:

    ssh user@ YOUR _ CONTAINER _ IP
    password : user

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: privilege_escalation_security_shells/0x00_what_the_shell
    File: 1-flag.txt

