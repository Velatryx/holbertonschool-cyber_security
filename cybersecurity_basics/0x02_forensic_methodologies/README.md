Resources
Read or watch:

    What is Computer Forensics
    What is SEIM
    Ethical Insights: IT Forensics, Ethics and Risks
    Digital Forensics and Incident Response
    Digital Forensics Methodologies
    What is Digital Forensics and Why Is It Important?
    The Digital Forensic Investigation Process
    Basic Steps in Forensic Analysis of Unix Systems

References:

    ACPO
    SWGDE
    DFRWS
    ISFCE
    IJDE
    NIST
    Forensic Focus

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What is digital forensics?
    Why is ethics important in digital forensics?
    What are common ethical issues in digital forensics?
    What is the role of integrity in forensic analysis?
    How does one maintain objectivity in digital investigations?
    What are the ACPO principles for computer forensics?
    How do you ensure evidence is admissible in court?
    What is chain of custody and why is it crucial?
    What are the stages of the digital forensic process?
    How does one document findings in a forensic report?
    What are some standard digital forensic methodologies?
    How does one handle digital evidence to preserve its integrity?
    What are some common tools used in digital forensics?
    What organizations set standards for digital forensic practices?
    How do you stay current with evolving technology in forensics?
    What are the legal implications of digital forensic investigations?

Requirements
General

    Allowed editors: vi, vim, emacs
    All analyses should be performed on Linux (Kali, ParrotOS, or Ubuntu 22.04+).
    Maintain a README.md at the project root summarizing your findings.

Tasks
0. The Case of the Mysterious Image

Welcome to your first foray into the world of digital forensics.
Your mission is to employ forensic analysis tools to reveal any concealed information or metadata, guiding your understanding of forensic concepts and methodologies.

Scenario:

You've been provided an image file (download), that is believed to contain crucial evidence related to an ongoing investigation.
Your objective is to analyze this image for hidden metadata or embedded information that could provide leads or insights into the case.

    Examine Metadata:
        Utilize exiftool to thoroughly analyze the image file's metadata.
    Identify Anomalies:
        Look for any unusual or suspect metadata entries that could suggest the owner name.
    Submission example:

        $ cat 0-mystery.txt
        `John_Doe`

Repo:

    GitHub repository: holbertonschool-cyber_security
    Directory: cybersecurity_basics/0x02_forensic_methodologies
    File: 0-mystery.txt

