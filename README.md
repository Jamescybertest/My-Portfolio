# Project 1: Responding to a Malware Attack

## Description

This project simulates a real-world cybersecurity incident response process triggered by a malware attack that caused a critical service outage. The simulation focuses on detecting the intrusion, analyzing log data, identifying the vulnerability (Spring4Shell), and documenting the response. The exercise mimics how a Security Operations Center (SOC) analyst would respond to such threats using basic log analysis and incident handling steps.

---

## Objective

- Analyze firewall logs to detect unusual activity.
- Identify and explain the exploit (Spring4Shell) used by the attacker.
- Create a firewall rule that identifies and blocks HTTP traffic containing key Spring4Shell payload elements
- Document the incident with a detailed postmortem report.
- Demonstrate the steps taken to contain and mitigate the threat.

---

## Tools & Technologies Used

- Python (for basic scripting)
- Firewall logs (simulated data)
- Text editor (Notepad)

---

## Skills Gained

- Threat detection and analysis
- Incident response procedures
- Root cause analysis
- Writing an executive summary and technical report
- Understanding of Spring4Shell vulnerability
- Familiarity with log formats and alert indicators

---

## Project Structure
Project1-Responding-to-Malware/
│
├── firewall_logs/ # Simulated log files
├── postmortem_report.md # Incident report
├── spring4shell_summary.txt # Exploit explanation
├── screenshots/ # Optional evidence screenshots
└── README.md # This documentation


---

## Sample Report Summary

> **Incident Summary:**  
> On March 20, 2022, a critical service outage occurred due to a remote code execution attack exploiting the Spring4Shell vulnerability on exposed infrastructure.  
>  
> **Detection:** Abnormal activity was detected via firewall logs and customer complaints.  
>  
> **Response:** SOC and network teams worked together to isolate affected systems and patch the vulnerable service.  
>  
> **Status:** Resolved within 2 hours. Root cause: unpatched Spring Framework exposed to the internet.

---

## How to Use

1. Review the `firewall_logs` to spot abnormal requests or exploit patterns. ( Open `firewall_Infrastructure list` to examine HTTP traffic for abnormal requests or known exploit patterns).
2. Open the `CVE Record.txt` to read the CVE Report and understand the vulnerability and how it is exploited
3. Run the Firewall Rule (Python Script) Navigate to the folder containing `firewall_server.py`, then run the firewall simulation Terminal: "python firewall_server.py". This will start an HTTP server that listens for incoming requests and checks for exploit patterns. Open another Terminal tab and run the exploit "test_request.py". The firewall will detect and Block http request status 403.
4. Open the `postmortem_Report` to learn how the incident was handled.

---

## Why This Matters in Cybersecurity

This exercise mirrors the real responsibilities of a Tier 1 SOC Analyst — detecting and triaging incidents, recognizing attack vectors, and clearly documenting actions. It builds a solid foundation for aspiring blue team professionals.

---



