
2. Hijack the Service - Exploit Weak Permissions
Your target machine is Virtual Machine (VM): LAB03

    The password for the student account is : Student

A service running with elevated privileges has weak file permissions. You’ve identified that it loads a DLL from a writable directory, giving you an opportunity to hijack it and escalate your privileges.

Can you hijack the service by exploiting the weak permissions and loading a malicious DLL to gain SYSTEM access?

Try to use this to get the flag from the superAdministrator:

Example of DLL code :

    SprintCSPDLL.

use win 10 RpcClient to execute the dll :

    WIN10RpcClient.exe.

1. Run privcheck

    Execute privcheck in the terminal to check for services with weak permission .

2. Check for writable path

    Review privcheck check the output for any writable paths.

3. Generate a DLL

    Create a DLL file.
    Write code to add user with admin prev privilege .
    Compile the DLL.

4. Copy DLL to Confluence bin

    Copy the DLL to the writable paths.

5. Trigger DLL with RPCClient

    Use RPCClient to load and execute the DLL.

6. Retrieve flag

    Flag Location: C:\User\superAdministrator\Desktop
