# 🔎 TCP Open Ports Checker

A multithreaded **Python TCP port scanner** that checks which ports are open on a target IP address.

The script scans all TCP ports from **1 to 65536**, displays progress in the terminal, and saves all discovered open ports into a file for later review.

It also includes a **terminal banner**, colored output, and a progress bar to make the scanning process easier to follow.

---

# ✨ Features

* 🔍 Scans **all TCP ports (1–65536)**
* ⚡ **Multithreaded scanning** for faster results
* 📊 **Progress bar** using `tqdm`
* 🎨 **Colored terminal output**
* 🖥️ **ASCII banners** using `pyfiglet`
* 💾 Automatically saves results to a file
* 📁 Creates a results folder automatically
* 🧵 Uses Python **threading** for simultaneous port checks

---

# 🧰 Requirements

* Python **3.7+**

### Python Modules

The script uses the following modules:

Built-in modules:

* `socket`
* `threading`
* `os`

External modules:

* `tqdm`
* `pyfiglet`
* `termcolor`

---

# 📦 Installation

Clone the repository:

```
git clone https://github.com/krainium/tcp-open-ports-checker.git
cd tcp-open-ports-checker
```

Install required dependencies:

```
pip install tqdm pyfiglet termcolor
```

Or create a **requirements.txt**:

```
tqdm
pyfiglet
termcolor
```

Then install with:

```
pip install -r requirements.txt
```

---

# 🚀 Usage

Run the script:

```
python port-scanner.py
```

You will be prompted to enter a target IP address:

```
Enter the target IP address:
```

Example:

```
Enter the target IP address: 192.168.1.1
```

The scanner will begin checking all TCP ports.

---

# 📂 Output

All open ports will be saved in:

```
opened-ports/open.txt
```

Example output file:

```
Target-IP: 192.168.1.1

Port 22 is opened!
Port 80 is opened!
Port 443 is opened!
```

---

# 🖥 Example Terminal Output

```
TCP OPEN PORTS CHECKER VERSION 1
SCRIPT MADE BY KRAINIUM

Scanning:  45%|███████████████ | 30000/65536 ports

Port 22 is open
Port 80 is open
Port 443 is open

Port scan complete
```

---

# ⚠️ Disclaimer

This tool is intended for:

* Educational purposes
* Network diagnostics
* Security testing on systems **you own or have permission to scan**

Do **NOT** use this tool to scan networks or servers without authorization.

---

# 📂 Project Structure

```
tcp-open-ports-checker/
│
├── port-scanner.py
├── requirements.txt
├── opened-ports/
│   └── open.txt
└── README.md
```

---

# 👨‍💻 Author

Krainium
GitHub: https://github.com/krainium

---

# 📜 License

MIT License
