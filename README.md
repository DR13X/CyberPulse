# CyberPulse

**Cybersecurity Intelligence CLI — Termux Edition**

Lightweight, rootless, terminal-only tool that aggregates live cybersecurity news, attacks, CVEs, breaches, malware, tools, and threat intelligence for students and researchers.

## Features

- Pure terminal CLI (no GUI, no web dashboard, no server)
- Live RSS + public API fetches (nothing stored after exit)
- Rich-powered colored output
- 18 menu options covering news, attacks, exploits, CVEs, breaches, malware, tools, TI, AI/web/cloud/mobile/network security, bug bounty, CTF, trends, and daily briefing
- Graceful handling of offline / failed sources
- Designed for Android Termux (also works on any Linux/macOS with Python 3)

## Requirements

- Python 3.8+
- Internet access
- Packages: `requests`, `feedparser`, `rich`

## Termux Installation

```bash
pkg update
pkg install python git
git clone https://github.com/DR13X/CyberPulse.git CyberPulse   # or copy the folder
cd CyberPulse
chmod +x install.sh
./install.sh
```

Or manually:

```bash
pip install -r requirements.txt
python cyberpulse.py
```

Optional launcher (created by `install.sh`):

```bash
cyberpulse
```

## Usage

```bash
python cyberpulse.py
```

Main menu:

```
============================================================
                 CYBERPULSE
          CYBERSECURITY INTELLIGENCE
              TERMUX EDITION
============================================================
[1]  Latest Cybersecurity News
[2]  Latest Cyber Attacks
...
[0]  Exit
```

Select a number. Data is fetched live. Press Enter to return to the menu. Choose `0` to exit.

## Project Structure

```
CyberPulse/
├── cyberpulse.py      # Entry point / main menu
├── sources.py         # RSS feeds & public API URLs
├── news.py            # HTTP/RSS fetch helpers
├── ui.py              # Rich terminal UI
├── vulnerabilities.py # CVE / CISA KEV
├── attacks.py
├── breaches.py
├── malware.py
├── tools.py           # GitHub + news
├── research.py        # TI, AI, web, cloud, mobile, network, bug bounty, CTF
├── trends.py          # Trends + daily briefing
├── requirements.txt
├── install.sh
└── README.md
```

## Design Principles

- **No database / no SQLite / no MongoDB / no JSON cache**
- **No login, no backend, no permanent storage**
- **No scanning, exploiting, or attacking** — read-only public information
- Failures of individual sources never crash the app
- All data lives only in temporary Python variables until exit

## Sources (examples)

- The Hacker News, BleepingComputer, Krebs on Security, Dark Reading, SecurityWeek
- CISA advisories & KEV catalog (JSON)
- CVEFeed.io, Zero Day Initiative
- Cisco Talos, Mandiant, Check Point Research, Malwarebytes, Securelist, etc.
- GitHub public search API for recently updated security repositories

## License

For educational and research use. Always verify critical information from primary sources.
