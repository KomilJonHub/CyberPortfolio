# Lab01 — Incident Response: File and Data Integrity Checks

**Role in Simulation:** SOC Analyst “Mike” (Branch Office IT)  
**Environment:** Cisco Packet Tracer network + Ubuntu CSE-LABVM  
**Type:** Simulated cyberattack and incident response in a virtual environment

---

## 📝 Scenario

In this virtual lab, I stepped into the role of **Mike**, the IT support at the branch office of a fictional organization.  
One morning, the branch network started showing signs of a **ransomware attack** — an ominous message appeared on one of the office machines, demanding payment to unlock files.  

The organization suspected that client files had been stolen and possibly tampered with. My mission was clear:

- Recover and verify the integrity of the client data.
- Investigate the scope of the compromise.
- Provide forensic evidence for management.
- Recommend security improvements to prevent this from happening again.

Even though this was a **controlled, virtual environment**, I treated it like a real-world incident — following a structured **Incident Response workflow** from detection to containment, analysis, and reporting.

---

## 🎯 Objectives

1. Retrieve **baseline hash values** from HQ for all client files.  
2. Download the latest copies from HQ to the branch for comparison.  
3. Detect any **tampering** using MD5 hashing.  
4. Verify the authenticity and integrity of a sensitive finance file using **HMAC-SHA256**.  
5. Escalate findings to my supervisor and preserve all evidence.

---

## 🧰 Tools & Commands Used

- **Packet Tracer** – to simulate the branch and HQ networks.
- **Ubuntu Linux CLI** – for file analysis and cryptographic checks.
- **`md5sum`** – to generate and compare file hashes.
- **`openssl dgst -sha256 -hmac <key>`** – to compute and verify HMAC.
- **FTP client** – used intentionally in the simulation to highlight its insecurity.

---

## 🔍 Step-by-Step Investigation

### **1) Confirming the breach**
I began by accessing my branch workstation and was greeted by a **ransomware-style message** — a clear indicator that something serious had happened.  
The attackers claimed files had been encrypted and demanded payment.  
![](./screenshots/02_branch_office_ransomware_screen.png)

In a real-world situation, this is the point where you **contain the incident** — isolate affected systems and prevent further spread. But in this lab, my goal was to **investigate**.

---

### **2) Collecting baseline integrity data**
Before touching any possibly compromised files, I retrieved **baseline MD5 hashes** from HQ — the “known-good” fingerprints for each client file.  
These would be my benchmark to determine if files had been altered.  
![](./screenshots/01_initial_hmac_check.png)

---

### **3) Pulling fresh copies from HQ**
Using FTP (as per the simulation), I downloaded six client files from HQ:  
`NEclients.txt`, `NWclients.txt`, `Nclients.txt`, `SEclients.txt`, `SWclients.txt`, and `Sclients.txt`.  
![](./screenshots/03_ftp_data_exfiltration_branch.png)  
![](./screenshots/04_branch_local_dir_listing.png)

In reality, FTP should **never** be used for sensitive transfers — it’s unencrypted and easily intercepted. The simulation intentionally used it to show the risk.

---

### **4) Previewing the data**
Opening one of the client files revealed **personally identifiable information** (names, contact details, etc.). Even in a simulation, it was easy to see how damaging this would be in a real breach.  
![](./screenshots/05_viewing_stolen_client_data_branch.png)

---

### **5) Detecting tampering with hashing**
I computed MD5 hashes for each of the branch’s client files and compared them to the HQ baselines.

- `NEclients.txt` – **match** ✅  
- `NWclients.txt` – **match** ✅  
- `Nclients.txt` – **mismatch** ❌ (altered)  
- `SEclients.txt` – **mismatch** ❌ (altered)  
- `SWclients.txt` – **mismatch** ❌ (altered)  
- `Sclients.txt` – **match** ✅

![](./screenshots/07_northwest_clients_hash_verification.png)  
![](./screenshots/08_southeast_clients_hash_verification.png)  
![](./screenshots/09_southwest_clients_hash_verification.png)

---

### **6) Validating the finance file with HMAC**
One critical file, `income.txt`, needed **both integrity and authenticity** verification.  
I used a shared secret (`cisco123`) with HMAC-SHA256 to compute its cryptographic signature.  
The computed HMAC matched the original — confirming it was unaltered and authentic.  
![](./screenshots/06_hmac_verification_branch_file.png)

---

### **7) Checking HQ systems**
To understand the attack scope, I also connected to HQ via FTP and confirmed that files there were accessible over the same insecure channel — a major vulnerability in this simulated environment.  
![](./screenshots/10_hq_data_exfiltration.png)

---

## 📑 Findings

- **Tampered files:** `Nclients.txt`, `SEclients.txt`, `SWclients.txt`  
- **Untouched files:** `NEclients.txt`, `NWclients.txt`, `Sclients.txt`  
- **Finance file:** `income.txt` passed HMAC verification (unaltered and authentic).  
- **Protocol risk:** FTP in use — unencrypted, vulnerable to interception and tampering.

---

## 🧠 Lessons Learned

- Always maintain a **baseline hash inventory** for critical files.
- Use **HMAC or digital signatures** for authenticity checks — hashes alone can be forged.
- Replace FTP with **SFTP/FTPS** for secure file transfers.
- Incorporate **central logging and SIEM monitoring** to catch integrity breaches faster.
- Preserve and document **all evidence** for post-incident review.

---

## 📂 Evidence

All investigation screenshots are stored in the `./screenshots` folder.  
An optional [`evidence_hashes.txt`](./evidence_hashes.txt) file lists baseline vs. current hashes.

---

## 💡 Why this matters

This lab was more than just following instructions — it was an **end-to-end incident simulation** where I got to act as a SOC analyst responding to a real threat scenario.

I had to think like an investigator:
- Confirm the attack.
- Gather and preserve evidence.
- Validate integrity with cryptographic methods.
- Communicate findings and recommend preventive measures.

It’s exactly the type of **practical, hands-on experience** I want to bring into my work as a cybersecurity professional.
