
1. Privilege Escalation through Cron Job Misconfiguration

The goal of this challenge is to gain elevated privileges on the linux machine. Make sure to enumerate properly the running processes, scheduled tasks, services, permissions and user management in order to find a weakness that can be exploited to gain root permission on the machine.

Environment:

    Target File:/root/flag.txt

    Vulnerable Area: Misconfigured cron jobs or writable scripts executed by cron with root privileges.

    Permissions: The script is writable by your user.

    Once root privileges are obtained, access the flag file and read its contents.

target machine for this task:

    cyber shell 0x02 inux privesc task2
