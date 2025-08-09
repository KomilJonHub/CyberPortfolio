# Lab01 — Incident Response: File and Data Integrity Checks

**Role:** SOC Analyst (simulated)  
**Environment:** Cisco Packet Tracer + Ubuntu CSE-LABVM (VirtualBox)  
**Scenario Type:** Simulated cyberattack investigation and response

---

## 🔍 Objective
In this lab, I simulated a real-world incident involving suspected tampering of client data files after a cyberattack.  
The goal was to:

1. **Recover files** from a backup after the attack.
2. **Verify integrity** of all client files using hashing (MD5) to detect tampering.
3. **Escalate** the incident to a supervisor and provide forensic evidence.
4. **Use HMAC-SHA256** to validate a sensitive finance file for both authenticity and integrity.

---

## 🧰 Tools & Commands Used
- **Packet Tracer** — to simulate the network, endpoints, and servers.
- **Linux CLI (CSE-LABVM)** — hashing and HMAC verification.
- **`md5sum`** — to generate and compare file hashes.
- **`openssl dgst -sha256 -hmac <key>`** — to compute and verify HMAC.
- **FTP client** — for simulated file transfers (lab environment only).

---

## 🛠 Key Steps Performed

### 1) Recover files after the simulated cyberattack
- Accessed the branch office server from Mike’s PC.
- Collected **baseline MD5 hashes** from the HQ server for all client files.  
  ![](./screenshots/01_initial_hmac_check.png)

### 2) Download backup files from HQ to branch
- Used FTP to pull six client files (`NEclients.txt`, `NWclients.txt`, `Nclients.txt`, `SEclients.txt`, `SWclients.txt`, `Sclients.txt`).  
  ![](./screenshots/03_ftp_data_exfiltration_branch.png)  
  ![](./screenshots/04_branch_local_dir_listing.png)

### 3) Detect tampered files using hashing
- Generated MD5 hashes for each file on the branch PC.  
- Compared against baseline hashes — identified mismatches (tampering).  
  ![](./screenshots/07_northwest_clients_hash_verification.png)  
  ![](./screenshots/08_southeast_clients_hash_verification.png)  
  ![](./screenshots/09_southwest_clients_hash_verification.png)

### 4) Escalate to supervisor
- Sent an email alert to Sally (supervisor) about the breach.
- Transferred the compromised file to Sally’s workstation for further analysis.

### 5) Verify finance file with HMAC-SHA256
- Computed HMAC for `income.txt` using the shared secret `cisco123`.  
- Matched with the original HMAC to confirm the file was **unaltered**.  
  ![](./screenshots/06_hmac_verification_branch_file.png)

---

## 📑 Findings
- **Tampered files:** `Nclients.txt`, `SEclients.txt`, `SWclients.txt`
- **Intact files:** `NEclients.txt`, `NWclients.txt`, `Sclients.txt`
- **Finance file:** `income.txt` passed HMAC verification.

**Likely cause:** Data exfiltration and modification over unencrypted FTP.

---

## 🧠 Lessons Learned
- **Hashes** detect changes but can’t confirm authenticity.
- **HMAC** adds authenticity, making it harder for attackers to replace files undetected.
- **FTP is insecure** — use SFTP/FTPS for all file transfers.
- Maintain **baseline hashes** for all critical files and store them securely.
- Escalation and evidence preservation are key parts of incident response.

---

## 📸 Screenshots
All evidence screenshots are stored in the `./screenshots` folder and named in investigation order:
1. `01_initial_hmac_check.png`
2. `02_branch_office_ransomware_screen.png`
3. `03_ftp_data_exfiltration_branch.png`
4. `04_branch_local_dir_listing.png`
5. `05_viewing_stolen_client_data_branch.png`
6. `06_hmac_verification_branch_file.png`
7. `07_northwest_clients_hash_verification.png`
8. `08_southeast_clients_hash_verification.png`
9. `09_southwest_clients_hash_verification.png`
10. `10_hq_data_exfiltration.png`

---

## 📂 Related Files
- [`evidence_hashes.txt`](./evidence_hashes.txt) — baseline vs. current hashes for all files.
