
0. Unlocking security, one exploit at a time!
Securing Your Shop's Admin Dashboard: Charting a Course through Vulnerability Waters ⚓️!

Shielding Shop Security..

Welcome to the gateway of Server-Side Request Forgery SSRF, where you'll embark on a journey through the digital landscape of vulnerabilities, set against the backdrop of our meticulously designed shop website. Your mission commences with probing the foundational element of SSRF vulnerabilities: uncovering potential gateways to unauthorized requests.

Before diving into the main challenge, let's get you familiar with SSRF vulnerabilities. SSRF occurs when an attacker can make the server perform requests to arbitrary destinations on their behalf, often exploiting how URLs and parameters are handled. By learning about SSRF, we can start to uncover hidden security risks in systems. Let's dive into the world of SSRF vulnerabilities and become experts at navigating the digital world.

Your mission is to test and secure our internal admin dashboard by identifying and exploiting potential SSRF vulnerabilities.

    Target Application: ShopAdmin
    Initial Endpoint: http://web0x08.hbtn/

Useful instructions:
1. Log into ShopAdmin, it is a shopping website, there is a lot of article.
2. The challenge is about the SSRF vulnerability in check reduction functionality.
3. You can click on one article and we see that we can do a check reduction.
4. Param articleApi is vulnerable.
5. This App is Forwarded on Port 3000 

Hints: Harness the power of Burp Suite to uncover SSRF vulnerabilities.

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: web_application_security/0x08_ssrf
    File: 0-flag.txt

Score of the task
