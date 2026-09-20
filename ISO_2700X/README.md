# Information Security Management System (ISMS) Assessment Report

---

## 1. Introduction

### 1.1 Overview

The company recently adopted an Information Security Management System (ISMS) structured around the ISO/IEC 27001 framework. This initiative demonstrates a clear commitment to safeguarding organizational data, ensuring business continuity, and managing operational risks.

Following the initial implementation, an internal audit was conducted to evaluate how effectively the operational processes align with ISO/IEC requirements. While foundational framework elements are present, the audit identified notable operational gaps that require direct remediation before formal certification or external surveillance.

### 1.2 Purpose and Scope

The goal of this report is to evaluate the internal audit findings, map each gap to specific ISO/IEC 27001 clauses and controls, and outline practical corrective actions.

**Scope:**

* Operational asset management workflows and inventory repositories.
* Physical and environmental security controls protecting critical zones (data closets, server rooms, and technical infrastructure).
* Data retention, backup management, and offsite storage operational controls.

---

## 2. Non-Conformities and Corrective Actions

### Finding 1: Incomplete Asset Management and Documentation

#### Non-Conformity Analysis

The internal audit revealed that only a subset of company assets is formally documented and tracked. Unmapped assets create blind spots in vulnerability management, patch routines, and incident handling. You cannot secure what you do not track.

#### Standard Violations

* **ISO/IEC 27001:2022 Clause 8.1 (Operational Planning and Control):** The organization failed to control the processes needed to meet information security requirements across all operational assets.
* **ISO/IEC 27002:2022 Control A.5.9 (Inventory of Information and Other Associated Assets):** Assets associated with information and information processing facilities are not fully identified, inventoried, or maintained.

#### Recommended Corrective Actions

1. **Deploy Automated Discovery Tools:** Implement network scanning tools to discover and catalog all connected hardware, software, and cloud assets into a central Configuration Management Database (CMDB).
2. **Establish Asset Ownership:** Assign a designated owner to each asset class responsible for classification, access permissions, and lifecycle management.
3. **Draft an Asset Management Policy:** Publish clear guidelines defining what qualifies as an asset, acceptable use terms (Control A.5.10), and mandatory check-in/check-out workflows for hardware.

---

### Finding 2: Insufficient Physical Access Controls for Critical Areas

#### Non-Conformity Analysis

Physical security controls guarding server rooms and core network closets were found to be weak or inconsistently enforced. Unauthorized physical access directly bypasses logical controls, exposing equipment to tampering, theft, or deliberate disruption.

#### Standard Violations

* **ISO/IEC 27002:2022 Control A.7.1 (Physical Security Perimeters):** Physical protection perimeters are not defined or enforced effectively around sensitive operational zones.
* **ISO/IEC 27002:2022 Control A.7.2 (Physical Entry Controls):** Critical areas lack adequate access restrictions, authentication mechanisms, and logging for personnel entry.

#### Recommended Corrective Actions

1. **Implement Two-Factor Physical Access:** Secure critical infrastructure doors with electronic badge readers coupled with biometric or PIN verification. Remove key-based manual locks where possible.
2. **Establish Access Log Reviews:** Mandate electronic entry logging for all secure areas. Configure the system to retain logs for at least 90 days and schedule bi-weekly administrative reviews.
3. **Formalize Visitor Access Management:** Enforce a policy requiring all non-cleared visitors to sign in at reception, display visible badges, and remain escorted by authorized personnel at all times inside critical areas (Control A.7.3).

---

### Finding 3: Poorly Defined Backup and Storage Management Procedures

#### Non-Conformity Analysis

Backup processes and data storage guidelines are vague, loosely documented, and lack standardized schedules. Without reliable, verified backups, the organization remains highly vulnerable to ransomware, system corruption, and catastrophic hardware failures.

#### Standard Violations

* **ISO/IEC 27001:2022 Clause 8.1 (Operational Planning and Control):** Lack of operational criteria and formal documentation for routine data protection workflows.
* **ISO/IEC 27002:2022 Control A.8.13 (Information Backup):** Backup copies of information, software, and system images are not created or tested regularly in line with an agreed topic-specific policy.

#### Recommended Corrective Actions

1. **Implement the 3-2-1 Backup Strategy:** Retain 3 total copies of critical data across 2 different media types, with 1 copy stored securely offsite or in an immutable cloud repository.
2. **Automate and Encrypt Backups:** Configure automated daily incremental and weekly full backups. Mandate AES-256 encryption for data at rest and in transit (Control A.8.24).
3. **Conduct Quarterly Restoration Drills:** Establish a schedule to test backup integrity through full system restoration tests every quarter. Document test results to prove Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) can be met.

---

## 3. Additional Recommendations (ISO/IEC 27002 Controls)

To further reinforce the ISMS beyond the immediate audit findings, the following supplementary controls from ISO/IEC 27002:2022 should be integrated into your security roadmap:

| Control | Description | Practical Application & Risk Reduction |
| --- | --- | --- |
| **A.5.15 Access Control** | Rules to control physical and logical access to information and associated assets. | Implement Role-Based Access Control (RBAC) and the principle of least privilege. This prevents employees from accessing sensitive files or systems outside their job scope, containing potential internal threats. |
| **A.8.8 Management of Technical Vulnerabilities** | Timely evaluation and patching of system security vulnerabilities. | Schedule automated weekly vulnerability scans across all endpoints and servers. Establishing a mandatory 14-day patch window for critical CVEs reduces the exposure window for external exploits. |
| **A.5.24 Information Security Incident Management Planning** | Preparation and workflows for detecting, reporting, and responding to incidents. | Create an Incident Response Plan (IRP) with clear roles and severity matrices. Running annual tabletop exercises ensures the team can isolate systems quickly during a breach, cutting downtime and potential data loss. |

---

## 4. Conclusion

The audit findings point to functional gaps in basic operational practices rather than systemic failure of the ISMS design. The core infrastructure for ISO/IEC 27001 compliance exists, but daily execution requires tighter controls around asset tracking, physical access enforcement, and backup verification.

Addressing these non-conformities requires shifting from informal routines to documented, automated, and audited processes. By executing the corrective action plans and adopting the recommended 27002 controls, the organization can reduce operational risk, protect critical data assets, and prepare smoothly for formal ISO/IEC 27001 certification.

Continuous improvement relies on regular Plan-Do-Check-Act (PDCA) cycles. Executive support in funding these remediation steps will directly preserve organizational resilience and build trust with clients.

---

## 5. References

1. **ISO/IEC 27001:2022** - *Information security, cybersecurity and privacy protection — Information security management systems — Requirements.*
2. **ISO/IEC 27002:2022** - *Information security, cybersecurity and privacy protection — Information security controls.*
3. **NIST Special Publication 800-53 (Rev. 5)** - *Security and Privacy Controls for Information Systems and Organizations.*
