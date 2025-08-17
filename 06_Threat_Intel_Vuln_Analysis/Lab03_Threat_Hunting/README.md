# Lab03 – Threat Hunting

## Introduction
This lab simulates a **real-world threat hunting investigation** where the task was to uncover signs of malicious activity, identify persistence mechanisms, and confirm evidence of **data exfiltration**.  
Threat hunting goes beyond relying on automated alerts — it requires proactively digging into logs, processes, and network behavior to uncover subtle Indicators of Compromise (IoCs) that adversaries attempt to hide.  

By completing this lab, I demonstrated the ability to:  
- Analyze **Windows Event Viewer logs** for DNS anomalies and malicious queries.  
- Investigate **PowerShell execution and persistence** through scheduled tasks.  
- Use **Linux tools** to reveal attacker scripts and outbound connections.  
- Correlate findings with **firewall logs** to confirm data exfiltration.  
- Document IoCs and deliver structured findings.  

---

## Objective
The primary objective was to detect and analyze a **multi-step intrusion scenario**, including:  
1. Identifying suspicious DNS activity pointing to possible command-and-control (C2) communication.  
2. Investigating PowerShell activity and persistence mechanisms on Windows hosts.  
3. Analyzing Linux netstat results and malicious bash scripts.  
4. Reviewing firewall logs for signs of large-scale data exfiltration.  
5. Correlating host-based evidence with network traffic to confirm the attack chain.  

---

## Lab Environment
The lab was conducted in a controlled cybersecurity training environment with simulated attack artifacts. It included:  
- **Windows 10 endpoint** with Event Viewer and PowerShell.  
- **Linux (Kali) environment** for attacker-side scripts and network analysis.  
- **Firewall logs** to capture exfiltration attempts.  

This setup reflects a realistic SOC workflow where multiple data sources must be investigated and correlated.  

---

## Tools and Techniques Used
- **Windows Event Viewer**  
  - Focused on DNS Client Events (Event IDs: 1001, 3010).  
  - Used keyword searches to identify suspicious queries.  

- **PowerShell**  
  - Inspected suspicious scripts (`lab04demo2.ps1`, `lab04demo3.ps1`).  
  - Queried for scheduled tasks to detect persistence.  

- **Linux Command-Line (Kali)**  
  - Used `netstat` to view active malicious connections.  
  - Inspected `Lab04demo4.sh` exfiltration script.  

- **Firewall Logs**  
  - Reviewed outbound traffic for anomalies.  
  - Pinpointed specific internal IP responsible for exfiltration.  

- **Threat Hunting Methodology**  
  - Hypothesis-driven investigation: Start from anomalies → test assumptions → confirm with multiple data points.  

## Investigation Walkthrough

### 1. Windows Event Viewer – DNS Activity
We began by reviewing **DNS Client Events** in Windows Event Viewer to look for abnormal queries.  
- Event **ID 1001** showed the DNS server being dynamically assigned to `10.1.16.1`.  
- Event **ID 3010** revealed repeated suspicious DNS queries to a known malicious domain: `badsite.ru`.

This confirmed that the compromised host was attempting outbound communication to a malicious external server.  

📸 Screenshot: [Suspicious DNS Query – badsite.ru](./screenshots/16.png)  

---

### 2. PowerShell Activity & Persistence
Further investigation focused on **PowerShell scripts** executed on the endpoint.  
- A script named **`lab04demo2.ps1`** executed a brute-force style loop until termination.  
  📸 Screenshot: [lab04demo2.ps1 Execution](./screenshots/12.png)  

- Another script, **`lab04demo3.ps1`**, demonstrated persistence by scheduling itself to run indefinitely under the SYSTEM account.  
  📸 Screenshot: [lab04demo3.ps1 Scheduled Task Persistence](./screenshots/2.png)  

This confirmed the attacker had established persistence by abusing Windows scheduled tasks.

### 3. Linux Attacker Scripts & Connections
Switching to the **Linux (Kali) environment**, we analyzed attacker-side artifacts.  

- Running `netstat -np --protocol=inet` revealed multiple **active connections** from the compromised Windows host (`10.1.16.2`) to the attacker’s C2 server (`10.1.16.1:443`).  
  📸 Screenshot: [Malicious Connections Observed via netstat](./screenshots/7.png)  

- A malicious bash script named **`Lab04demo4.sh`** was discovered.  
  - It redirected the malicious domain to the attacker’s IP in `/etc/hosts`.  
  - It launched a reverse connection to `ca.ad.structurereality.com` over port 443 in an infinite loop.  
  📸 Screenshot: [Malicious Bash Script Revealed](./screenshots/14.png)  

This confirmed that the attacker used Linux tools to maintain C2 communication and prepare exfiltration.

---

### 4. Firewall Log Review – Data Exfiltration
Next, we pivoted to **firewall logs** to confirm signs of data theft.  
- Large outbound transfers were observed from internal IP `10.1.16.2`.  
- Traffic volume reached over **1029 MB**, indicating massive exfiltration attempts.  

📸 Screenshot: [Firewall Logs Confirm Exfiltration](./screenshots/10.png)  

This confirmed that **10.1.16.2** was the compromised host responsible for exfiltrating sensitive data.

---

## Findings & Conclusion
Through multi-source analysis, we confirmed the full attack chain:  
1. **Initial Access & C2** – DNS logs revealed communication with malicious domain `badsite.ru`.  
2. **Persistence** – PowerShell scripts established scheduled task execution under SYSTEM privileges.  
3. **C2 & Exfiltration** – Linux-based malicious scripts maintained outbound connections.  
4. **Data Theft** – Firewall logs confirmed large-scale exfiltration from `10.1.16.2`.  

### ✅ Key Skills Demonstrated
- Correlated **Windows Event Viewer, PowerShell, Linux netstat, and firewall logs**.  
- Identified **Indicators of Compromise (IoCs)** across multiple environments.  
- Traced attacker behavior from **initial compromise → persistence → data exfiltration**.  
- Produced a structured investigation report suitable for SOC workflows.  

📌 This lab highlights the importance of **threat hunting beyond alerts** — correlating artifacts across systems is essential to uncover stealthy adversary tactics.
