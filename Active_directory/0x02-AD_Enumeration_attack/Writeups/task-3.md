### Mission: Finding information which default tooling does not show: `adminDescription`.

**Blueprint:** `ldapsearch -H ldap://[Target IP] -x -D "[Bind DN]" -w '[Password]' -b "[Base DN]" "[Search Filter]" [Attributes to Return]`

**Command:**

```bash
ldapsearch -H ldap://192.168.56.20 -x -D "CN=student,CN=Users,DC=PENTESTLAB,DC=local" -w 'password1234' -b "DC=PENTESTLAB,DC=local" "(adminDescription=*)" adminDescription

```

---

### Analysis & Cyber Attack Context

In typical Active Directory enumeration passes, tools like NetExec or basic scripts target common organizational unit (OU) containers and explicit user/group object classes (`(objectClass=user)`, `(objectClass=group)`). They request standard attributes such as `sAMAccountName`, `description`, or `memberOf`.

However, non-standard or administrative properties—specifically those stamped on the **root Domain Object itself** (e.g., `DC=PENTESTLAB,DC=local`)—are completely bypassed unless explicitly queried or parsed via a full BloodHound ingestion pipeline (`SharpHound`).

* **The Vulnerability:** Information exposure via object schema attributes. Administrators occasionally utilize administrative tagging fields like `adminDescription` or `adminDisplayName` on structural container objects to track internal flags, deployment scripts, or legacy operational notes, under the assumption that standard users won't look at the root object's schema properties.
* **The Fix:** Strict access control lists (ACLs) should be audited at the root domain level to ensure standard domain users cannot read sensitive administrative attributes on structural objects.

---

### Recovered Flag

**Flag:** `PVFLAG0{D0M41N_M4PP3D_W1TH_P0W3RV13W_F0}`
