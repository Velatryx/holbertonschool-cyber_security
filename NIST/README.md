```markdown
# Computer Security Incident Response Plan (CSIRP)

**Framework Alignment:** NIST SP 800-61 Rev. 2  
**Document Owner:** Incident Response Coordinator  
**Classification:** Operational Security Document  
**Target Audience:** Security Operations Center (SOC), Systems Engineering, Legal, Executive Leadership  

---

## 1. Context, Purpose, and Scope

### Background
This document was established following an alert involving unauthorized access to core network segments and potential exfiltration of sensitive organizational data. Initial indicators showed unexpected lateral movement between non-production systems and a restricted SQL database server (`db-prod-02.internal.net`), originating from an obfuscated IP address range (`192.0.2.45`).

### Purpose
The objective of this Incident Response Plan is to establish a standardized, repeatable framework for discovering, containing, eradicating, and recovering from security events. Following these protocols minimizes business disruption, limits impact on customer data, meets regulatory obligations, and strengthens defense capabilities against future threat vectors.

### Scope
This plan applies to all computing assets, endpoints, network devices, cloud environments (AWS, Azure), software applications, and physical locations owned or managed by the organization. It covers all personnel, including full-time employees, contractors, third-party vendors, and temporary staff.

---

## 2. Incident Response Process (NIST SP 800-61 Lifecycle)


```

+-----------------------------------------------------------------------+
|                            1. PREPARATION                             |
+-----------------------------------------------------------------------+
|
v
+-----------------------------------------------------------------------+
|                      2. DETECTION & ANALYSIS                          |
+-----------------------------------------------------------------------+
|
v
+-----------------------------------------------------------------------+
|             3. CONTAINMENT, ERADICATION & RECOVERY                    |
+-----------------------------------------------------------------------+
|
v
+-----------------------------------------------------------------------+
|                      4. POST-INCIDENT ACTIVITY                        |
+-----------------------------------------------------------------------+

```

### Phase 1: Preparation
Preparation is the foundation of incident response. It ensures tools, infrastructure, and team members are ready before an incident happens.

* **Tooling and Infrastructure:** Maintain centralized log collection (SIEM), endpoint detection and response (EDR) agents across all hosts, network monitoring tools, and forensic software tools.
* **Communication Channels:** Set up out-of-band communication channels (e.g., dedicated Signal groups or isolated messaging instances) in case primary corporate channels (Slack, email) are compromised.
* **Access Control:** Maintain privilege-isolated incident response accounts with multi-factor authentication (MFA) pre-configured.
* **Training and Exercises:** Run bi-annual tabletop exercises and routine technical simulation drills to test response readiness under realistic conditions.

### Phase 2: Detection and Analysis
This phase focuses on identifying potential security events, verifying whether an actual incident is underway, and assessing its impact.

#### Indicators vs. Precursors
* **Precursors:** Signs that an attack may happen in the future (e.g., port scans against external firewalls, web application vulnerability testing from IP `198.51.100.12`).
* **Indicators:** Signs that an attack is happening now or has already occurred (e.g., system alerts showing credential dumping on server `srv-app-01`, unauthorized file exports via unexpected protocols).

#### Triage and Severity Classification
Upon receiving an alert, analysts perform initial validation to filter out false positives. Confirmed incidents are assigned a severity rating:

| Severity Level | Criteria | Required Initial Response |
| :--- | :--- | :--- |
| **Low (Severity 3)** | Isolated malware attempt blocked by EDR; single endpoint affected without data loss. | Within 4 hours |
| **Medium (Severity 2)** | Unauthorized access to a non-critical system; potential privilege escalation without clear data exfiltration. | Within 1 hour |
| **High / Critical (Severity 1)** | Confirmed access to sensitive databases, ransomware deployment, or active domain admin compromise. | Immediate (within 15 minutes) |

#### Analysis Actions
1. **Scope Determination:** Search SIEM logs and EDR console for compromised accounts, IP addresses, hashes, or malicious process names across the enterprise.
2. **Evidence Preservation:** Take volatile memory (RAM) dumps and forensic disk images of affected systems prior to taking them offline. Ensure proper chain-of-custody tracking forms are filled out and signed.

### Phase 3: Containment, Eradication, and Recovery
Once an incident is identified, teams must prevent further damage, remove the adversary's access, and restore affected services safely.

#### Containment Strategies
* **Short-Term Containment:** Isolate affected endpoints at the network level via EDR. Revoke compromised credentials, disable hijacked API keys, and terminate active user sessions immediately.
* **Long-Term Containment:** Apply temporary firewall blocks, update network segmentation boundaries, reissue access certificates, and implement temporary enhanced monitoring on adjacent systems.

#### Eradication
* Remove malware artifacts, malicious scheduled tasks, registry modifications, and persistence mechanisms.
* Rebuild compromised operating systems from secure, validated base images rather than attempting manual cleanup.
* Patch underlying vulnerabilities that enabled the initial access vector.

#### Recovery and Restoration
* Restore database systems and applications from verified, uninfected backups.
* Reconnect systems to the operational network using a phased rollout plan.
* Apply strict monitoring rules to restored systems for 30 days to detect potential re-infection or missed backdoors.

### Phase 4: Post-Incident Activity
The post-incident phase focuses on identifying operational gaps and updating defenses to prevent recurring incidents.

* **Incident Timeline Assembly:** Build an exact chronological sequence of events, from initial threat vector entry to final containment.
* **Post-Incident Review:** Host a lessons-learned meeting within 5 business days of incident closure.
* **Artifact Archival:** Store all logs, forensic images, chat transcripts, and analyst notes in an encrypted repository for legal, compliance, and auditing purposes.

---

## 3. Team Roles and Responsibilities

During an incident, clear ownership prevents miscommunications and delays.

### Role Definitions

#### Incident Commander (IC)
* Coordinates overall incident response execution.
* Makes critical strategic decisions (e.g., taking high-value production environments offline).
* Manages resource allocation and assigns technical leads.

#### Technical Lead / Forensics Specialist
* Leads hands-on investigation, threat hunting, and log analysis.
* Captures forensic artifacts and determines initial attack vectors.
* Executes technical containment and eradication actions.

#### Infrastructure / Sysadmin Lead
* Assists with system isolation, firewall configuration updates, and backup restoration.
* Provides system architecture context to technical analysts.
* Manages account lockouts and privilege resets across Active Directory / IAM systems.

#### Communications Lead
* Handles internal communications to staff and executives.
* Drafts external messaging, customer advisories, and PR statements in coordination with Legal.

#### Legal & Compliance Advisor
* Determines legal reporting requirements (e.g., GDPR, CCPA, HIPAA).
* Interface with law enforcement agencies and regulatory bodies.

---

### RACI Matrix

| Phase | Incident Commander | Technical Lead | Infrastructure Lead | Communications Lead | Legal Advisor |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Preparation** | **A** | **R** | **R** | **C** | **C** |
| **Detection & Analysis** | **A** | **R** | **C** | **I** | **I** |
| **Containment** | **A** | **R** | **R** | **I** | **C** |
| **Eradication** | **A** | **R** | **R** | **I** | **I** |
| **Recovery** | **A** | **C** | **R** | **C** | **I** |
| **Post-Incident Analysis**| **A** | **R** | **C** | **C** | **C** |

*Legend: **R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed*

### Role Transfer Protocols
If an incident spans multiple shifts, a formal handover briefing must occur:
1. Active status brief covering containment posture, unverified leads, and current risks.
2. Formal transfer of the Incident Lead role within the tracking tool.
3. Notification to all team members updating them on who is currently acting as Incident Commander.

---

## 4. Post-Incident Analysis & Continuous Improvement

### Post-Mortem Meeting Agenda
The post-mortem meeting must focus on processes and facts rather than placing blame. Key questions to answer include:
* Exactly what happened, and at what times?
* How well did staff and response procedures perform?
* Which technical indicators failed to trigger alerts?
* What early indicators could have helped us detect the breach sooner?
* What communication roadblocks hindered the team?

### Actionable Deliverables
1. **Formal Incident Report:** A comprehensive summary detailing total downtime, financial impact, root cause, and remediation timelines.
2. **SIEM Rule Tuning:** Update correlation rules and detection logic to spot similar technical behaviors automatically.
3. **Control Enhancements:** Implement missing security controls, such as adding network micro-segmentation or enforcing stricter MFA rules.
4. **Policy and Playbook Updates:** Update incident handling steps based on unexpected challenges encountered during the incident.

---

## 5. Conclusion

A structured, NIST-aligned Incident Response Plan provides a clear roadmap when a security event occurs. Relying on ad-hoc decision-making during a critical breach increases downtime, exposes sensitive data to exfiltration, and amplifies organizational risk. 

To remain effective, this plan must be treated as a living document. It requires quarterly operational reviews, routine updates to contact rosters, and regular tabletop testing to adapt to changing threat landscapes.

---

## 6. References

* **NIST Computer Security Resource Center:** [NIST SP 800-61 Rev. 2: Computer Security Incident Handling Guide](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
* **NIST Cybersecurity Framework (CSF 2.0):** [Govern, Identify, Protect, Detect, Respond, Recover Framework](https://www.nist.gov/cyberframework)
* **CISA Incident Response Resources:** [Cybersecurity & Infrastructure Security Agency Playbooks](https://www.cisa.gov/resources-tools/services/incident-response-services)
* **FIRST Security Frameworks:** [Forum of Incident Response and Security Teams Guidelines](https://www.first.org/resources/guides/)

```
