nxc ldap 192.168.56.20 -u labuser -p 'P@ssw0rd123!' --groups

ldapsearch -H ldap://192.168.56.20 -x -D "CN=labuser,CN=Users,DC=PENTESTLAB,DC=local" -w 'P@ssw0rd123!' -b "DC=PENTESTLAB,DC=local" "(&(objectCategory=group)(|(cn=Domain Admins)(cn=Enterprise Admins)(cn=Backup Operators)))" "*" "+"
