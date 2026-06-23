
2. BloodHound Collection and Analysis: Mapping the AD Attack Surface with BloodHound

Objective:

BloodHound collects all Active Directory relationships and object properties into a graph database. Unlike ldapsearch, it visualizes attack paths and exposes properties across all objects simultaneously. A flag has been embedded in a property that BloodHound surfaces during collection.

Your mission:

Run bloodhound-python to collect all AD data Import the ZIP into the BloodHound GUI

Navigate object properties to find the **hidden flag**

Tool: bloodhound-python+ BloodHound GUI

Hint: After importing the data, search for specific users in BloodHound. Click on a node and inspect its properties panel not all attributes appear in LDAP queries but do appear in BloodHound node details.

Flag location: A property of a user object visible in BloodHound node details after collection
