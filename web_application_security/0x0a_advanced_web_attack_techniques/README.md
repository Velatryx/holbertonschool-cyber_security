Introduction:

"Security is not a product, but a process." Bruce Schneier

Advanced web attacks rarely look dangerous at first glance. A normal-looking request, a slightly unusual log entry, or an unexpected file access pattern can each signal a vulnerability hiding in plain sight. Developing the discipline to observe application behavior in real time and interpret those signals accurately is what separates a thorough penetration tester from a surface-level scanner.
Context:

In this project, you will move beyond basic vulnerability identification into active exploitation of advanced web attack techniques. During a realistic testing scenario, you will encounter subtle behavioral signals: anomalous HTTP requests, unexpected server-side file access, and unusual application responses. Each signal is a clue. Your objective is to follow those clues systematically identifying, analyzing, and exploiting vulnerabilities before a real attacker can.

By the end of this project, you will be able to:

    Recognize behavioral indicators of advanced web vulnerabilities in live applications
    Apply structured methodology to move from discovery to exploitation
    Document findings with the precision expected in professional penetration testing reports

Resources
Read or watch:

    What is cross-site scripting (XSS)?
    How to Prevent Cross-Site Scripting (XSS) in JavaScript?
    XSS Injection
    Insecure deserialization
    PHP Deserialization
    reventing insecure deserialization vulnerabilities
    Server-side template injection
    Server-side template injection2
    Server-Side Template Injection vulnerability: what it is and how to prevent it

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    the impact and risk of the vulnerabilities in web applications.
    Identify and Explain Types of XSS.
    Explain how XSS injections work and how they exploit web applications.
    Implement Prevention Techniques.
    Recognize the importance of secure coding practices.
    Integrate security checks into the development lifecycle to prevent vulnerabilities.

Requirements
General

    Allowed editors: vi, vim, emacs.
    All your scripts will be tested on Kali Linux.
    All your files should end with a new line (Why?)
    A README.md file, at the root of the folder of the project, is mandatory
    Use the IP address in the tasks, not the hostname

Endpoints & Base Code

    Task 0 Endpoint : http://web0x0a.task0.hbtn/
    Task 1 Endpoint : http://web0x0a.task1.hbtn/
    Task 2 Endpoint : http://web0x0a.task2.hbtn/
    Task 3 Endpoint : http://web0x0a.task3.hbtn/
    Task 4 Endpoint : http://web0x0a.task4.hbtn/
    Base Code: All tasks base code

Tasks
0. Advanced XSS Challenge - Photo Gallery Exploitation

Explore and exploit an XSS vulnerability in the provided photo gallery web application to capture the administrator's cookie. This task simulates a real-world web attack scenario, focusing on advanced techniques in web application security.

Holberton School has created a photo gallery app for users to share their favorite pictures. While regular users can view and suggest photos, only the admin has the authority to approve and add them. Your mission is to exploit a vulnerability in the Suggestion Page to capture the admin's cookie using a malicious payload. Successfully retrieving the admin's cookie will allow you to obtain the flag, which is the main objective of this task.

Instructions:

    Review the provided index.html file for potential vulnerabilities.
    Look for parameters in the JavaScript code that can be manipulated (e.g., holberton parameter in the eval function).
    Use the identified vulnerability to craft a malicious URL that executes your payload when accessed by the admin.
    Ensure the payload sends the admin's cookies to your external webhook.

Tips:

    Inspect the JavaScript carefully to identify how inputs are processed.
    Utilize tools such as the browser's developer console and Webhook.site to assist in payload testing and capturing cookies.
    Pay close attention to eval() and how the parameter holberton is being used in the provided HTML code.
    Review any browser behaviors (e.g., cross-origin requests) that may affect your payload delivery.

    Initial Endpoint: http://web0x0a.task0.hbtn
    Suggestion Endpoint: Suggestion
    Monitor Webhook for Cookies: Webhook
    Code base: Index.html

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: web_application_security/0x0a_advanced_web_attack_techniques
    File: 0-flag.txt

