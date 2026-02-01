Resources
Read or watch:

    Content discovery
    Content Discovery for Web Application Security
    Content Discovery: Understanding Your Web Attack Surface
    What are the content discovery
    OWASP Testing Guide: Content Discovery
    Exploiting: Content Discovery

References:

    dirb
    nikto
    sfuzz
    wfuzz
    gobuster
    dirbuster
    feroxbuster

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What is content discovery?
    Why is content discovery important?
    How does directory bruteforcing work?
    What is Gobuster and how is it used?
    Explain the use of Burp Suite in content discovery.
    How does OWASP ZAP assist in content discovery?
    What are wordlists and how are they used in content discovery?
    Describe the purpose of tools like DirBuster.
    What are hidden directories and files in web security?
    Explain fuzzing in the context of web security.

Requirements
General

    Allowed editors: vi, vim, emacs.
    All your scripts will be tested on Kali Linux.
    All your scripts should be exactly one line long ($ wc -l file should print 1)
    All your files should end with a new line (Why?)
    A README.md file, at the root of the folder of the project, is mandatory
    For this project, your focus will be on the target Cyber - WebSec 0x04.

Tasks
0. Manual Discovery - Secrets in Plain Sight

Your goal is to uncover a hidden flag by thoroughly exploring the site's structure.

Use all available discovery methods, including analyzing files such as robots.txt, sitemap.xml, and favicon.ico

    Target Machine: Cyber - WebSec 0x04
    Target Endpoint: http://web0x04.hbtn/

1 . Sitemap Exploration

Start by reviewing the sitemap located at /sitemap.xml. The sitemap may reveal unusual or hidden routes not linked from anywhere else on the site.

One of these routes contains your flag.

2 . Additional Discovery

Investigate any common files such as robots.txt or favicon.ico, as they may contain further clues or hidden paths.

Useful Instructions
1.Start by navigating to /robots.txt. Look for any Disallow entries that might hint at hidden or restricted paths. These paths could lead to interesting or hidden resources.
2.Access /sitemap.xml. Sitemaps are used to help search engines index web content, but they may also reveal hidden resources. Find the resource that is not linked from anywhere else on the site to discover your flag.
3.Download the site's favicon.ico and analyze it using tools or online resources like the OWASP favicon database. By matching the favicon to known frameworks, you might uncover more information about the site.
4.Pay close attention to details in each file. Each file could contain direct paths or subtle hints that lead to the next step in your discovery process.
5.Utilize online tools for favicon analysis and comparison to help identify the framework and speed up your search for hidden resources.

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: web_application_security/0x04_content_discovery
    File: 0-flag.txt

