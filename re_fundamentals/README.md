

For this project, we expect you to look at these concepts:

    RE Fundamentals

Introduction

"Every program tells a story. Reverse engineering is how you learn to read it."

Modern software runs everywhere - on computers, servers, mobile devices, and embedded systems. Sometimes the source code is not available, but the behavior of the program still matters. Security professionals must be able to analyze applications, understand how they work, and identify hidden functionality or vulnerabilities. Learning reverse engineering builds deep technical thinking. It teaches how to examine compiled programs, trace execution flow, and understand system behavior step by step. These skills are essential for malware analysis, vulnerability research, incident response, and software security testing. Understanding what a program does internally allows defenders to detect threats, verify software integrity, and protect critical systems.
Context

During a security investigation, a company discovered an unknown program running on one of its servers. The application had no documentation, and its purpose was unclear. System logs showed unusual network connections, but there was no obvious error or alert. Security analysts began examining the file carefully. By analyzing the program structure and monitoring its behavior, they identified hidden functions that were collecting system information and sending it to an external server. The issue was not visible to normal users, but detailed analysis revealed the risk.

Resources
Read or watch:

    OpenSecurityTraining: Intro to x86
    Reverse Engineering Fundamentals
    Ghidra Tutorial Series

Books and Articles

    Reverse Engineering for Beginners:
    Practical Reverse Engineering
    The IDA Pro Book

Tools

    IDA Pro
    Ghidra
    Radare2
    x64dbg
    OllyDbg

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    What is reverse engineering in software?
    Why is reverse engineering important in malware analysis, vulnerability research, and software compatibility?
    What is disassembly, and how does it translate machine code into assembly language?
    What is decompilation, and how does it differ from disassembly?
    How does code flow analysis help in understanding program logic?
    What techniques are used to identify functions in binaries?
    What are the common disassemblers (IDA Pro, Ghidra, Radare2), and how do they differ?
    How do debuggers (GDB, x64dbg, OllyDbg) help in reverse engineering?
    How do decompilers (Hex-Rays, RetDec) convert assembly code to higher-level languages?
    What is the role of static analysis tools (Binwalk, Strings) in reverse engineering?
    What are the main executable file formats (PE, ELF, Mach-O), and how are they analyzed?
    How do Control Flow Graphs (CFGs) help visualize program execution?
    How does cross-referencing help track functions, variables, and data within a program?
    What are common anti-reverse engineering techniques (obfuscation, packing, anti-debugging)?
    How can you bypass anti-reverse engineering techniques?
    How to use common reverse engineering techniques in real-world CTF challenges.

Requirements
General

    Allowed tools: objdump, readelf, ldd.
    All analyses should be conducted in a controlled environment, like a VM or sandbox.
    Ensure that all files are backed up regularly during the analysis process.
    All your scripts must be executable and runnable on Kali Linux.
    You should avoid using hardcoded values for paths; utilize relative paths instead.
    Make sure to validate the integrity of the binaries before analyzing them.
    All analysis findings should be organized and clearly formatted for easy reference.
    For this project, your focus will be on the target target_binary
    You are not allowed to use online tools or services for your analysis; everything must be done locally.

