# GhostTap — Endpoint Surveillance Simulation Framework

GhostTap is a modular, stealth-oriented surveillance simulation tool built in Python. It was inspired by the tactics employed by real-world state-sponsored threat groups such as Fancy Bear (APT28), whose high-profile campaigns — including phishing, silent data collection, and endpoint exploitation — demonstrated how a single link or executable could exfiltrate massive amounts of sensitive data.

This project simulates such techniques legally and locally, showing how endpoint devices (camera, microphone, keyboard) can be silently monitored, with encrypted payloads securely exfiltrated to a custom Flask-based C2 server for automated decryption and classification.

The project is intended strictly for educational and demonstration purposes — as a hands-on deep dive into stealthy data pipelines, modular logging systems, and secure file transmission protocols.

Learn more: [APT28 Profile – MITRE ATT&CK](https://attack.mitre.org/groups/G0007/)


---

## 🔧 Features

- 🧠 **Modular Agent Architecture** — Independent threaded loggers (cam, mic, keylogger)
- 🔐 **Strong Encryption** — All data encrypted using `Fernet` symmetric encryption
- 🌐 **Secure Data Transfer** — Encrypted files sent via HTTP POST to a Flask C2 server
- 🧩 **Decryption + Classification** — Server auto-decrypts and sorts logs by type
- 🪶 **Lightweight & Stealthy** — Minimal output; logs are captured silently
- 📂 **Clean Project Structure** — Well-organized directories for agent/server roles

---

## 🖼️ System Architecture

```
+-------------+         [Encrypted Upload]         +-------------+
|   Agent     | --------------------------------→ |    Server   |
| (macOS app) |                                    | (Flask API) |
+-------------+                                    +-------------+
     |                                                    |
     |                                                    |
     |                                                    |
     |→ cam_logger.py      → logs/*.jpg.enc   → decrypt   → static/cam/
     |→ mic_logger.py      → logs/*.wav.enc   → decrypt   → static/mic/
     |→ key_logger.py      → logs/*.txt.enc   → decrypt   → static/keylogs/
```

---

## 📁 Project Structure

```
GhostTap/
├── agent/
│   ├── cam_logger.py
│   ├── mic_logger.py
│   ├── key_logger.py
│   ├── uploader.py
│   ├── encryptor.py
│   ├── secret.key
│   ├── logs/
│   └── main.py
├── server/
│   ├── server.py
│   ├── decryptor.py
│   ├── secret.key
│   ├── received/
│   └── static/
│       ├── cam/
│       ├── mic/
│       └── keylogs/
└── README.md
```

---

## 🚀 How It Works

### Agent Side:
1. Each logger runs in its own thread (`cam_logger`, `mic_logger`, `key_logger`)
2. Captured data is written to disk → encrypted → sent to server
3. All logs are auto-deleted locally after upload

### Server Side:
1. Flask route `/upload` receives `.enc` files
2. Files are decrypted using `Fernet` and classified based on file signature
3. Final files are saved in `/static/{cam|mic|keylogs}` directories

---

## 🧪 Technologies Used

- **Python 3.11+**
- `opencv-python` for webcam feed
- `sounddevice` + `scipy` for mic capture
- `pynput` for keylogging
- `cryptography` for encryption (Fernet)
- `Flask` for server & decryption endpoint

---

## ⚠️ Disclaimer

> This project is intended strictly for **personal educational use**, interview discussion, and research into secure data handling and background task design. Do not use or distribute any surveillance tools or monitoring software without clear, informed consent and compliance with applicable laws.

---

## 🗂 Possible Future Features

- 📊 Web dashboard to view logs
- 🗜️ Compressed upload batches
- ☁️ Cloud-hosted C2 deployment
- 🖼️ Preview thumbnails & waveform visualization
- 📦 `.app` / `.exe` packaging with `pyinstaller`

---

## 📚 Learnings

This project showcases:
- Real-world multithreaded architecture
- Data pipeline construction
- Encryption-first design thinking
- Secure file I/O
- Minimal agent-server communication models

---

## 🧠 Author

**Ozan Gokberk**  
Graduate Software Engineer & Fullstack Developer  
[London, UK] – Reachable on request
