# Network Discovery & Traffic Analysis Suite

A Python-based cybersecurity mini-project built over a 4-day sprint. This suite consists of a multi-threaded **TCP Port Scanner** for asset discovery and a live **Network Packet Sniffer** for traffic analysis and network monitoring.

## 🚀 Features
* **Multi-Threaded Scanning**: Scans a specified range of TCP ports rapidly using Python's native `threading` and `socket` modules.
* **Live Traffic Decoders**: Identifies and categorizes Layer 3/4 network protocols (TCP, UDP, ICMP) in real time.
* **PCAP Generation**: Automatically captures, structures, and outputs live network traffic into standard `.pcap` files compatible with **Wireshark**.

---

## 🛠️ Project Structure & Day-by-Day Development

* **Day 1: Setup & Foundations** -> Built a Python virtual environment (`venv`), mapped out TCP connection structures, and installed Scapy and network adapter drivers.
* **Day 2: Port Scanner Engine (`scanner.py`)** -> Developed an asynchronous, multi-threaded script to sweep targets (e.g., `scanme.nmap.org`) for open services.
* **Day 3: Packet Sniffer Core (`sniffer.py`)** -> Implemented low-level network hooks using `scapy` to read network packets off the local network interface controller (NIC).
* **Day 4: Logging & Documentation** -> Expanded the sniffer functionality to log raw payload metrics straight to a persistent PCAP capture log file.

---

## 💻 Prerequisites & Setup

### Requirements
* **Python 3.x**
* **Npcap / WinPcap driver** (Required for Windows packet capturing. Must be installed with *WinPcap API-compatible mode* enabled).

### Deployment Steps
1. Clone or open the project folder in **VS Code**.
2. Open a Command Prompt (`cmd`) terminal and spin up the virtual environment:
   ```cmd
   python -m venv venv
   venv\Scripts\activate.bat
   ```
3. Install the required network analysis dependencies:
   ```cmd
   pip install scapy
   ```

---

## 📋 Tool Usage & Sample Output

### 1. Running the Port Scanner
Executes scanning routines to safely identify active network endpoints:
```cmd
python scanner.py
```
**Sample Output:**
```text
--------------------------------------------------
Scanning Target: scanme.nmap.org
Scanning started at: 2026-09-30 18:39:21.859978
--------------------------------------------------
[+] Port 22 is OPEN
[+] Port 80 is OPEN

Scanning complete.
```

### 2. Running the Packet Sniffer
*Note: This script must be run inside a console or editor session spawned with **Administrative Privileges**.*
```cmd
python sniffer.py
```
**Sample Output:**
```text
--------------------------------------------------
Starting Packet Sniffer... Capturing 50 packets.
Live traffic will print below, and save to a file.
--------------------------------------------------
[+] TCP Packet: 34.104.35.123 -> 10.22.19.184
[+] TCP Packet: 10.22.19.184 -> 34.104.35.123
[+] TCP Packet: 199.232.210.172 -> 10.22.19.184

--------------------------------------------------
Sniffing complete. Saving packets...
SUCCESS: Packets saved to 'captured_traffic.pcap'.
--------------------------------------------------
```

---

## 🛡️ Cybersecurity Context & Analysis
* **Offensive Insight**: Port scanning is a vital stage of reconnaissance (recon). Attackers map out target landscapes via tools like this to find open avenues (like port 22/SSH or port 80/HTTP) to launch vulnerability testing or exploits.
* **Defensive Insight**: Passive packet sniffers monitor active networks for anomalies, unencrypted text payloads, or unusual inbound traffic surges. The generated `.pcap` files provide security teams with deep audit trails for incident response forensics.

## ⚖️ Disclaimer
This software suite is developed strictly for **educational and defensive analysis purposes**. Scanning networks or harvesting packet traffic on infrastructure without explicit, written authorization from the system owners is illegal.
