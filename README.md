## holbertonschool-cyber_security

This repository contains my solutions, automation scripts, and lab writeups from the Holberton School Cybersecurity curriculum, structured across consecutive 3-month training sprints, 10 months (3 sprints), and foundation (1 month) in total.

---

## ⏳ Curriculum Timeline & Mapping

### 🏁 Sprint 1: Core Security Foundations
Focuses on low-level Linux administration, networking architecture, passive/active reconnaissance baselines, and initial web application flaws.

#### 📁 Linux & Core Foundations
* **`/cybersecurity_basics`**
  * Introduction to Cyber Security & Cryptography Basics (Key generation, SHA256 validation, `john`/`hashcat` configuration)
  * Forensic Ethics & Methodologies
* **`/linux_security`**
  * `0x00_linux_security_basics` – Network service auditing and firewall profiling
  * `0x01_permissions_sguid_sgid` – Auditing weak permissions, SUID/SGID bits, and loose sudo rules
  * `0x02_mandatory_access_control` – SELinux modes, contexts, and booleans
  * `0x03_protocols_servers` – Automated hardening and `iptables` script deployment

#### 📁 Network Reconnaissance & Analysis
* **`/network_security`**
  * `0x01_passive_reconnaissance` & `0x02_active_reconnaissance` – DNS parsing (`dig`), subdomain mapping (`subfinder`), and host tracking
  * `0x04_nmap_live_hosts_discovery` – Host discovery via ARP, ICMP, and TCP SYN/ACK pings
  * `0x05_wireshark_basics` – Packet and frame analysis, capturing scanner fingerprints

#### 📁 Web Infrastructure & AI Safety
* **`/web_application_security`**
  * `0x00_web_fundamentals` – HTTP headers, basic XSS payloads, and host header injection
  * `0x01_owasp_top_10` – Core application vulnerability tracking and decoding scripts
  * `0x02_burpsuite_fundamentals` – Intercepting, modifying, and replaying web traffic
  * `0x03_sql_nosql_injection` – Testing injection boundaries and automated extraction
  * `0x04_content_discovery` – Directory brute-forcing and asset identification
  * `0x05_upload_vulnerabilities` – Extension filtering and payload execution bypasses
* **`/cyber_prompt_injection`**
  * LLM context manipulation and basic prompt injection proofs-of-concept

---

### 🚀 Sprint 2: Enterprise Infrastructure & Advanced Exploitation
Shifts focus into Windows Active Directory networks, offensive scripting, advanced web exploitation vectors, and incident response automation.

#### 📁 Active Directory Architecture
* **`/Active_directory`**
  * `Theory` & `0x01-AD_Basics_And_Concepts` – Core architecture and components
  * `0x02-AD_Enumeration_attack` – Targeted service enumeration and credential abuse
  * `0x03-AD_LDAP` – Querying directory services for domain intelligence
  * `0x04-AD_BloudHound` – Graph-theory attack path tracking
  * `0x05-AD_PowerView` – Post-exploitation asset enumeration and object mapping

#### 📁 Advanced Scanning & Incident Response
* **`/network_security`**
  * `0x06_nmap_advanced_port_scans` – Null, Xmas, and Maimon custom scan logic
  * `0x07_nmap_post_port_scan_scripting` – Automating vulnerability scanning via NSE scripts (`vulners`)
* **`/web_application_security`**
  * `0x0b_web_application_fast_incident_response` – High-speed log analysis scripts (`count_attack.sh`, `attack_ip.sh`)
  * `0x0c_web_application_foresics` – Log forensics, system accounts auditing, and firewall tracking

#### 📁 Offensive Scripting, Flaws & Frameworks
* **`/scripting_cyber`**
  * `0x00-ruby_scripting` – Writing custom command-line utilities, HTTP clients, and password tools in Ruby
* **`/vulnerability_research_exploitation`**
  * `0x00_vulnerability` – CVE/CWE parsing, vulnerability tracking, and Nessus reporting
  * `0x03_metasploit_basics` & `0x04_metasploit_scripting` – Custom Ruby orchestration scripts (`automated_exploit_launcher.rb`)
* **Standard Vulnerability Modules (`/web_application_security`)**
  * `0x06_idor` – Insecure Direct Object References
  * `0x07_file_inclusion` – Local and Remote File Inclusions (LFI/RFI)
  * `0x08_ssrf` – Server-Side Request Forgery
  * `0x09_command_injection` – Command Injection vectors (including Log4Shell log analysis)
  * `0x0a_advanced_web_attack_techniques` – Authentication bypass and advanced request forging
* **Low-Level Exploitation (`/linux_security`)**
  * `0x04_buffer_overflow` – Heap parsing and basic memory execution control (`read_write_heap.py`)

---

### ⚡ Sprint 3: Advanced Host Interrogation, Reverse Engineering & GRC
Focuses on binary deep-dives, mobile application analysis frameworks, privilege escalation pipelines, and enterprise security compliance.

#### 📁 Shells & Privilege Escalation
* **`/privilege_escalation_security_shells`**
  * `0x00_what_the_shell` – Shell interactive mechanics, payload generation, and stabilization techniques
* *[Upcoming]* **Linux & Windows Privilege Escalation** – Kernel exploits, misconfigured services, token manipulation, and enumeration checklists

#### 📁 Reverse Engineering & Malware Analysis *[In Progress]*
* *[Upcoming]* **Reverse Engineering Fundamentals** – Assembly basics, disassembly, and control flow analysis
* *[Upcoming]* **Static & Dynamic Analysis** – Analyzing compiled binaries using tools like Ghidra, IDA, and GDB
* *[Upcoming]* **Malware Analysis** – Behavior tracking, signature matching, and basic sandboxing concepts

#### 📁 Mobile Application Security *[In Progress]*
* *[Upcoming]* **Mobile Fundamentals** – Android/iOS sandboxing models and app architecture basics
* *[Upcoming]* **Static & Dynamic Mobile Analysis** – Decompiling APKs/IPAs, tracking intent flaws, and utilizing runtime hooks (Frida/Objection)

#### 📁 Governance, Risk, Compliance & Ethics *[In Progress]*
* *[Upcoming]* **Frameworks & Standards** – Implementing and auditing controls across NIST, ISO 2700X, and GDPR
* *[Upcoming]* **Ethics in Cybersecurity** – Responsible disclosure models and operational ethics

---

## 📝 Lab Components

Directories generally contain three core files:
1. **Automation Scripts (`*.sh`, `*.rb`, `*.py`)** – Functional tools built to complete the objectives programmatically.
2. **Flag Logs (`*-flag.txt`)** – Verification strings captured upon successful box compromise.
3. **Tasks/Writeups (`*.md`)** – Personal reference documentation outlining technical details and mitigation steps.
