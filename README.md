# 🛰️ NOIS - Premium IP Intelligence System `v15.0`

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![UI](https://img.shields.io/badge/UI-Rich--CLI-red?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Audit-white?style=for-the-badge)

**NOIS** is a high-performance terminal utility designed for network diagnostics and geolocation intelligence. Developed as a professional-grade CLI tool, it offers a centered and visually optimized experience for gathering deep network data.

<img width="1115" height="624" alt="Ekran görüntüsü 2026-04-04 154146" src="https://github.com/user-attachments/assets/19f71386-2228-4b83-8a04-6518a6c174e3" />

---

## ⚠️ LEGAL DISCLAIMER & EDUCATIONAL PURPOSES

**This tool is strictly for EDUCATIONAL, RESEARCH, and ETHICAL TESTING purposes.**

1. **Usage:** The developer (**NOIS**) is not responsible for any misuse or illegal activities performed with this tool. 
2. **Compliance:** Users are solely responsible for complying with local and international laws regarding network privacy.
3. **Non-Malicious Intent:** This project was created to demonstrate Python's networking and TUI (Terminal User Interface) capabilities.

---

## 🌟 Key Features

* **🛡️ Self-Audit:** Instantly view your own public IP footprint.
* **🎯 Target Intelligence:** Retrieve country, city, coordinates, and ASN for any IP.
* **📦 Bulk Scanning:** Process multiple IPs with a real-time progress tracker.
* **🎨 Premium UI:** Fully centered layout with high-end ASCII art.
* **⚡ Rate-Limit Protection:** Built-in sleep cycles to prevent API bans.

---

## 💻 Installation (Terminal / Termux)

Run the following commands to install and launch the system:

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/noiserrr/NOIS---IP-Scanner
cd NOIS---IP-Scanner
pip install requests rich
python main.py
