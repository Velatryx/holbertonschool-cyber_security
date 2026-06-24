
3. ACL Enumeration & GenericAll Abuse

Access Control Lists (ACLs) in Active Directory define who can do what to which object. Every user, group, computer, and GPO has an ACLthat controls permissions. While most ACEs (Access Control Entries) are set correctly by default, misconfigurations are extremely common in real environments.

The most dangerous permission is GenericAll, which grants full control over an object. If account A has GenericAllover account B, then A can reset B's password, modify its attributes, add it to groups, or perform any other operation on it without B's knowledge.

-Instructions:

In this task, you will enumerate all non-default ACEs across the domain and look for dangerous permissions. Once you find a GenericAll misconfiguration, investigate the target account carefully the flag is stored in one of its attributes, readable only once you understand the ACL relationship.

Hint:

PowerView has a dedicated function to find interesting ACLs across the entire domain and resolve GUIDs to human-readable right names. Filter the results for the most dangerous permission type.
