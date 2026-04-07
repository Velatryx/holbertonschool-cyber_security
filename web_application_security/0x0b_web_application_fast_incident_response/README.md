Resources
Read or watch:

    What is incident response?
    What is cyber risk mitigation?
    (CIRP).
    Log Management Best
    understand attacker behavior and techniques.
    Security Tools and Alerts
    Endpoint Detection and Response
    What Is Log Monitoring? Benefits & Security Use Cases?
    Vulnerability Scanners

Learning Objectives

By the end of this project, you are expected to be able to explain the following to anyone, without the help of Google:

    What are the stages of web application incident response, and why is each stage important?

    How can web application attacks be quickly detected and identified?

    What are the effective methods for containing, eradicating, and recovering from web application incidents?

    What role does automation play in speeding up incident response?

    How should incidents be documented and communicated during response actions?

    Why are post-incident reviews significant, and how do they contribute to security improvements?

    How can detection and monitoring tools be utilized to identify potential web application incidents?

    What skills are necessary for accurately identifying and prioritizing threats in web applications?

    How can normal service operations be restored as quickly as possible to minimize the impact on business activities?

Requirements
General

    Allowed editors: vi, vim, emacs.
    All your scripts will be tested on Kali Linux.
    All your files should end with a new line (Why?)
    The first line of all your files should be exactly #!/bin/bash.
    A README.md file, at the root of the folder of the project, is mandatory
    You are not allowed to use backticks, &&, || or ;.
    All your files must be executable
    Ensure that $1 is used without quotes in your script to prevent unintended argument type alterations.

Files

Files Used in This Project

    logs.txt

Tasks
0. Identify the Attack Source

Create a Bash script to identify the IP address responsible for the most requests in a log file, which is likely the source of a Denial of Service (DoS) attack.

Functionality:

    Extract IP addresses from the log file.

    Count the occurrences of each IP address.

    Identify and print the IP address with the highest number of requests.

    Log File : logs.txt

TIP: see which Ip had the most requests

┌──(oumaima㉿hbtn-lab)-[…/web_application_security/0x0b_web_application_fast_incident_response]
└─$  ./0-attack_ip.sh
**.***.**.**

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: web_application_security/0x0b_web_application_fast_incident_response
    File: 0-attack_ip.sh

