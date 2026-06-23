### Our mission is to find the flag within a hidden property that Bloodhound does show.

However, I was unable to retrieve the flag using Bloodhound, because it did not actually collect the hidden property at all.

Still, I am providing the writeup for bloodhound data collection, and using it in GUI.

## First, let's collect the domain data. You cannot perform an anonymous search with Bloodhound to my knowledge using null user or pass like 
ldapsearch or nxc ldap.

Blueprint: bloodhound-python -u <"USER"> -p <"PASS"> -d <DOMAIN> -ns <TARGET_IP> -c All --zip (optionally you can add --dns-tcp for more reliable connection)

```Bash
bloodhound-python -u 'student' -p 'password1234' -d PENTESTLAB.local -ns 192.168.56.20 -c All --zip
```

It collects the domain info, and zips them. We import it by logging in to the GUI version of it on http://localhost:8080, sign in with the credentials (default: admin,admin)

Use Quick Upload to upload the zip folder;

Go to explore tab to start visualizing the data;

For example, type 'Users' on search bar, and select a node to visualize the nodes and connections. An example would seem like this:

<img width="2879" height="1419" alt="image" src="https://github.com/user-attachments/assets/aee3c2bc-537d-4bea-b41f-a25c2af3ea16" />


Simply, click on a node, go through the properties, or choose members and go through theirs.

---

However, to find the flag, I used:

```bash
nxc ldap -u 'student' -p 'password1234' --users --base-dn "DC=PENTESTLAB,DC=local--query "(|(wWWHomePage=*)(comment=*)(description=*))" "cn distinguishedName wWWHomePage comment description"
```

