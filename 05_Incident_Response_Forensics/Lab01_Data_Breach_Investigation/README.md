# Lab01 – Incident Response: Simulated Data Breach & File Integrity Investigation

## 🔍 Objective
Simulate a cyberattack, investigate tampered files, and validate data integrity using cryptographic hashing and HMAC. This lab showcases the **Incident Response workflow** end-to-end: detection → analysis → evidence collection → recommendations.

## 📂 Repo Placement
**This case study lives in:** `05_Incident_Response_Forensics/`  
Cross-referenced from: [`09_Cryptography_Encryption`](../../09_Cryptography_Encryption/) (hashing/HMAC concepts).

## 🧰 Tools Used
- Packet Tracer (network scenario & endpoints)
- Linux CLI: `md5sum`, `openssl dgst -sha256 -hmac <key>`
- FTP client (for simulated exfil/retrieval)

## 🧵 Scenario Summary
- Suspicious activity detected across branch/HQ endpoints.
- Client files may have been **altered and exfiltrated** via **FTP**.
- A **ransomware-style message** appeared on an endpoint.
- Tasked with confirming tampering, preserving evidence, and recommending controls.

## 🛠 Steps Performed
1. **Baseline Hashes** – Collected known-good hashes from HQ.  
   ![](./screenshots/01_hash_list_source.png)

2. **Verification** – Retrieved files from branch/HQ, computed and compared hashes.  
   ![](./screenshots/02_hash_verification.png)
   ![](./screenshots/03_ftp_download_branch.png)
   ![](./screenshots/04_ftp_download_hq.png)

3. **Evidence of Exfiltration / Tampering** – Confirmed mismatches and gathered artifacts.  
   ![](./screenshots/05_exfiltrated_data_preview.png)
   ![](./screenshots/06_ransomware_message.png)

4. **HMAC Validation** – Verified integrity of `income.txt` using SHA256-HMAC.  
   ![](./screenshots/07_hmac_sha256_income.png)

5. **Follow-up** – Logged outcomes and documented recommendations.  
   ![](./screenshots/08_hash_verification_followup.png)
   ![](./screenshots/09_hash_list_updated.png)
   ![](./screenshots/10_final_confirmation.png)

## ✅ Findings
- **Compromised files:** `Nclients.txt`, `SEclients.txt`, `SWclients.txt`
- **Safe:** `NEclients.txt`, `NWclients.txt`, `Sclients.txt`, `income.txt` (HMAC verified)

## 🧠 Lessons Learned
- Use secure transfer (SFTP/FTPS) instead of plain FTP.
- Maintain baseline hash inventories for integrity checks.
- Prefer HMAC over plain hashing for authenticity + integrity.

See: [`evidence_hashes.txt`](./evidence_hashes.txt)

