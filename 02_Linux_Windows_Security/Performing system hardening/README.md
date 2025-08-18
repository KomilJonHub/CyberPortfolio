
# Lab: Performing System Hardening

## 🔍 Scenario
In this applied lab, I worked on **system hardening** for Structureality Inc. across Windows and Linux systems.  
System hardening focuses on two key operations: **removing what isn’t needed** and **updating what is needed**.  
The challenge is iterative: update → remove → validate → repeat — which is exactly what we practiced.

## 🎯 Objectives
This lab aligns with CompTIA CySA+ objectives:
- **1.1**: Explain the importance of system and network architecture concepts in security operations  
- **2.5**: Explain concepts related to vulnerability response, handling, and management  

## 🧰 Tools & Environment
- **KALI Linux** (Debian-based, penetration testing build)  
- **DC10** (Windows Server 2019, Domain Controller)  
- **MS10** (Windows Server 2016)  
- **PC10** (Windows Server 2019 client)  
- Tools: Bash, Nano, wget, Windows CMD, Server Manager, Windows Defender Firewall  

---

## 🛠 Key Steps Performed

### 1. Managing Device Drivers (Windows Server)
System hardening begins with checking and maintaining device drivers to ensure no outdated/insecure components remain.

- Opened **Device Manager** and scanned for hardware changes.  
![Device Manager Scan](./screenshots/1.png)  

- Verified that the **CD-ROM driver** was already up-to-date.  
![Driver Status Up To Date](./screenshots/2.png)  

---

### 2. Manipulating Hosts File Resolution (Linux)
Edited `/etc/hosts` to control FQDN resolution — blocking, redirecting, and restoring correct resolution.

- Verified resolution with `wget` and checked current `/etc/hosts`.  
![Initial wget and hosts file](./screenshots/3.png)  

- Introduced a **false entry** using nano.  
![Editing hosts in nano](./screenshots/4.png)  

- Tested false resolution — connection failed due to wrong mapping.  
![wget failure from false entry](./screenshots/5.png)  

- Restored the correct mapping to 203.0.113.228 → resolution succeeded.  
![Corrected wget success](./screenshots/11.png)  

---

### 3. Removing Unneeded Applications and Services (Windows Server)
Eliminating unused software and insecure services reduces attack surface.

- Uninstalled **CPUID CPU-Z** via Programs and Features.  
![Uninstall CPUID](./screenshots/6.png)  

- Launched **Remove Roles and Features Wizard**.  
![Remove Roles and Features Wizard](./screenshots/7.png)  

- Removed the **FTP Server** role and service.  
![Removing FTP Service](./screenshots/8.png)  

---

### 4. Applying Firewall Rules (Windows Firewall with Advanced Security)
Restricted ICMP traffic to enforce security baselines.

- **Before hardening**: PC10 successfully pinged DC10.  
![Ping Success Before Firewall Block](./screenshots/9.png)  

- Configured inbound rules to **explicitly block ICMP Echo Requests**.  
![Firewall inbound rules block](./screenshots/12.png)  

- **After hardening**: ping requests from PC10 to DC10 timed out.  
![Ping Block After Firewall Rule](./screenshots/10.png)  
![Ping Block Verified](./screenshots/13.png)  

---

### 5. Setting File Permissions (Linux)
Applied secure file permissions using both symbolic and octal notation.

- Applied `chmod 710 demofile.sh` → limited to owner full access, group execute, no access for others.  
![chmod 710 demofile.sh](./screenshots/14.png)  

- Practiced symbolic notation (`u+x`, `g+w`, `go-r,u-x`) on **testfile.txt**.  
![Symbolic chmod on testfile.txt](./screenshots/15.png)  

- Practiced octal notation (`777`, `644`) to reset permissions.  
![Octal chmod examples](./screenshots/16.png)  

---

## 📸 Full Screenshot Walkthrough
All 16 screenshots are included in `./screenshots/` with contextual captions above.

---

## 🧠 Lessons Learned
- **Hardening is iterative**: update → remove → validate → repeat.  
- Hosts file manipulation shows how easily DNS can be overridden.  
- Removing unused software/services immediately reduces vulnerabilities.  
- **Firewall best practice**: use explicit **deny rules**, not just disabling allows.  
- Linux file permissions are foundational for controlling confidentiality, integrity, and availability.  

---

✅ **Relevance to Career**  
This lab demonstrates practical SOC analyst and GRC skills:  
- Applying security baselines across platforms  
- Documenting and validating changes  
- Connecting hardening techniques to compliance and operational security  
