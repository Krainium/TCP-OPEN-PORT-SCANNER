# TCP Open Ports Checker

Multithreaded Python TCP port scanner that checks which ports are open on a target IP address. Scans all TCP ports from 1 to 65536, displays live progress, and saves all discovered open ports to file.

---

## Features

- Scans all TCP ports (1–65536)
- Multithreaded for faster results
- Progress bar via `tqdm`
- Colored terminal output
- Auto-saves results to a results folder

---

## Requirements

- Python 3.7+

**External packages:**

```bash
pip install tqdm pyfiglet termcolor
```

Or via requirements file:

```bash
pip install -r requirements.txt
```

---

## Installation

```bash
git clone https://github.com/krainium/tcp-open-ports-checker.git
cd tcp-open-ports-checker
pip install tqdm pyfiglet termcolor
```

---

## Usage

```bash
python port-scanner.py
```

Enter the target IP when prompted:

```
Enter the target IP address: 192.168.1.1
```

The scanner starts immediately and shows live progress.

---

## Output

Open ports save to `opened-ports/open.txt`:

```
Target-IP: 192.168.1.1
Port 22 is opened!
Port 80 is opened!
Port 443 is opened!
```

---

## Project Structure

```
tcp-open-ports-checker/
  port-scanner.py
  requirements.txt
  opened-ports/
    open.txt
  README.md
```

---

## Disclaimer

For educational purposes, network diagnostics, and security testing on systems you own or have explicit permission to test. Unauthorized scanning of networks or systems may violate laws and policies.

---

## License

MIT
