
0. Privilege Escalation in Windows Environments
Objective

Your goal is to extract sensitive data from unattended files

Your target machine is Virtual Machine (VM): LAB01

    To locate unattended installation files, extract sensitive administrative credentials, and covertly gain access to retrieve a target flag.
    The password for the student account is : Student
    The following steps detail the functionality of the Python script and its execution process.

Write a script to resolve this task.
1. Typical File Locations

The script scans the following common locations for unattended installation files:

    sysprep.inf
    autounattend.xml
    Unattend.xml

2. Password Extraction

    Utilizes regular expressions to extract the <AdministratorPassword> <Value>(.*?)</Value> from the files.

3. Decoding

    Decodes the extracted password.

4. Admin Session

    Uses runas to establish an administrative session using the extracted credentials. to get the flag which is in the desktop of the Admin session
