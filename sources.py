"""
CyberPulse - RSS feed and public API sources configuration.
All sources are public and require no authentication.
"""

# General cybersecurity news
NEWS_FEEDS = [
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "News"},
    {"name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/feed/", "category": "News"},
    {"name": "Krebs on Security", "url": "https://krebsonsecurity.com/feed/", "category": "News"},
    {"name": "Dark Reading", "url": "https://www.darkreading.com/rss.xml", "category": "News"},
    {"name": "SecurityWeek", "url": "https://www.securityweek.com/feed/", "category": "News"},
    {"name": "The Record", "url": "https://therecord.media/feed/", "category": "News"},
    {"name": "CyberScoop", "url": "https://cyberscoop.com/feed/", "category": "News"},
    {"name": "Help Net Security", "url": "https://www.helpnetsecurity.com/feed/", "category": "News"},
]

# Attack / incident oriented feeds
ATTACK_FEEDS = [
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "Attacks"},
    {"name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/feed/", "category": "Attacks"},
    {"name": "Krebs on Security", "url": "https://krebsonsecurity.com/feed/", "category": "Attacks"},
    {"name": "The Record", "url": "https://therecord.media/feed/", "category": "Attacks"},
    {"name": "Dark Reading", "url": "https://www.darkreading.com/rss.xml", "category": "Attacks"},
]

# Exploit / PoC related
EXPLOIT_FEEDS = [
    {"name": "Zero Day Initiative", "url": "https://www.zerodayinitiative.com/rss/published/", "category": "Exploits"},
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "Exploits"},
    {"name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/feed/", "category": "Exploits"},
    {"name": "Project Zero", "url": "https://googleprojectzero.blogspot.com/feeds/posts/default", "category": "Exploits"},
]

# Vulnerability / CVE sources
CVE_FEEDS = [
    {"name": "CVE Feed Latest", "url": "https://cvefeed.io/rssfeed/latest.xml", "category": "CVE"},
    {"name": "CVE Feed High/Critical", "url": "https://cvefeed.io/rssfeed/severity/high.xml", "category": "CVE"},
    {"name": "CISA Advisories", "url": "https://www.cisa.gov/cybersecurity-advisories/all.xml", "category": "CVE"},
    {"name": "CISA Alerts", "url": "https://www.cisa.gov/cybersecurity-advisories/alerts.xml", "category": "CVE"},
    {"name": "Zero Day Initiative", "url": "https://www.zerodayinitiative.com/rss/published/", "category": "CVE"},
]

# CISA KEV JSON (public, no auth)
CISA_KEV_JSON = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

# Data breach sources
BREACH_FEEDS = [
    {"name": "Have I Been Pwned", "url": "https://feeds.feedburner.com/HaveIBeenPwnedLatestBreaches", "category": "Breaches"},
    {"name": "Krebs on Security", "url": "https://krebsonsecurity.com/feed/", "category": "Breaches"},
    {"name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/feed/", "category": "Breaches"},
    {"name": "The Record", "url": "https://therecord.media/feed/", "category": "Breaches"},
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "Breaches"},
]

# Malware / ransomware
MALWARE_FEEDS = [
    {"name": "Malwarebytes Labs", "url": "https://www.malwarebytes.com/blog/feed/index.xml", "category": "Malware"},
    {"name": "Securelist (Kaspersky)", "url": "https://securelist.com/feed/", "category": "Malware"},
    {"name": "WeLiveSecurity (ESET)", "url": "https://www.welivesecurity.com/feed/", "category": "Malware"},
    {"name": "Cisco Talos", "url": "https://blog.talosintelligence.com/rss/", "category": "Malware"},
    {"name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/feed/", "category": "Malware"},
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "Malware"},
]

# Threat intelligence
THREAT_INTEL_FEEDS = [
    {"name": "Cisco Talos", "url": "https://blog.talosintelligence.com/rss/", "category": "Threat Intel"},
    {"name": "Check Point Research", "url": "https://research.checkpoint.com/feed/", "category": "Threat Intel"},
    {"name": "Mandiant", "url": "https://www.mandiant.com/resources/blog/rss.xml", "category": "Threat Intel"},
    {"name": "Microsoft Security", "url": "https://www.microsoft.com/en-us/security/blog/feed/", "category": "Threat Intel"},
    {"name": "Crowdstrike", "url": "https://www.crowdstrike.com/en-us/blog/feed/", "category": "Threat Intel"},
    {"name": "Unit 42", "url": "https://unit42.paloaltonetworks.com/feed/", "category": "Threat Intel"},
    {"name": "The DFIR Report", "url": "https://thedfirreport.com/feed/", "category": "Threat Intel"},
]

# AI Security
AI_SECURITY_FEEDS = [
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "AI Security"},
    {"name": "Dark Reading", "url": "https://www.darkreading.com/rss.xml", "category": "AI Security"},
    {"name": "SecurityWeek", "url": "https://www.securityweek.com/feed/", "category": "AI Security"},
    {"name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/feed/", "category": "AI Security"},
    {"name": "Help Net Security", "url": "https://www.helpnetsecurity.com/feed/", "category": "AI Security"},
]

# Web Security
WEB_SECURITY_FEEDS = [
    {"name": "PortSwigger Research", "url": "https://portswigger.net/research/rss", "category": "Web Security"},
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "Web Security"},
    {"name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/feed/", "category": "Web Security"},
    {"name": "Dark Reading", "url": "https://www.darkreading.com/rss.xml", "category": "Web Security"},
    {"name": "Help Net Security", "url": "https://www.helpnetsecurity.com/feed/", "category": "Web Security"},
]

# Cloud Security
CLOUD_SECURITY_FEEDS = [
    {"name": "AWS Security Blog", "url": "https://aws.amazon.com/blogs/security/feed/", "category": "Cloud Security"},
    {"name": "Google Cloud Security", "url": "https://cloud.google.com/blog/topics/security/rss", "category": "Cloud Security"},
    {"name": "Microsoft Security", "url": "https://www.microsoft.com/en-us/security/blog/feed/", "category": "Cloud Security"},
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "Cloud Security"},
    {"name": "Dark Reading", "url": "https://www.darkreading.com/rss.xml", "category": "Cloud Security"},
]

# Mobile Security
MOBILE_SECURITY_FEEDS = [
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "Mobile Security"},
    {"name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/feed/", "category": "Mobile Security"},
    {"name": "Malwarebytes Labs", "url": "https://www.malwarebytes.com/blog/feed/index.xml", "category": "Mobile Security"},
    {"name": "Securelist", "url": "https://securelist.com/feed/", "category": "Mobile Security"},
    {"name": "WeLiveSecurity", "url": "https://www.welivesecurity.com/feed/", "category": "Mobile Security"},
]

# Network Security
NETWORK_SECURITY_FEEDS = [
    {"name": "Cisco Talos", "url": "https://blog.talosintelligence.com/rss/", "category": "Network Security"},
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "Network Security"},
    {"name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/feed/", "category": "Network Security"},
    {"name": "Dark Reading", "url": "https://www.darkreading.com/rss.xml", "category": "Network Security"},
    {"name": "Help Net Security", "url": "https://www.helpnetsecurity.com/feed/", "category": "Network Security"},
]

# Bug Bounty & Disclosures
BUG_BOUNTY_FEEDS = [
    {"name": "HackerOne Blog", "url": "https://www.hackerone.com/blog.rss", "category": "Bug Bounty"},
    {"name": "Bugcrowd Blog", "url": "https://www.bugcrowd.com/blog/feed/", "category": "Bug Bounty"},
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "Bug Bounty"},
    {"name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/feed/", "category": "Bug Bounty"},
    {"name": "PortSwigger Research", "url": "https://portswigger.net/research/rss", "category": "Bug Bounty"},
]

# CTF & Research
CTF_RESEARCH_FEEDS = [
    {"name": "CTFtime", "url": "https://ctftime.org/rss/upcoming/", "category": "CTF"},
    {"name": "Project Zero", "url": "https://googleprojectzero.blogspot.com/feeds/posts/default", "category": "Research"},
    {"name": "PortSwigger Research", "url": "https://portswigger.net/research/rss", "category": "Research"},
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "Research"},
    {"name": "Help Net Security", "url": "https://www.helpnetsecurity.com/feed/", "category": "Research"},
]

# Keywords used for filtering when a general feed is reused for a topic
KEYWORDS = {
    "attacks": [
        "attack", "ransomware", "phishing", "ddos", "breach", "compromise",
        "espionage", "supply chain", "account takeover", "intrusion", "hacked",
        "cyberattack", "campaign", "threat actor", "apt",
    ],
    "exploits": [
        "exploit", "poc", "proof-of-concept", "rce", "zero-day", "0day",
        "remote code", "privilege escalation", "vulnerability disclosed",
        "actively exploited", "weaponized",
    ],
    "breaches": [
        "breach", "data leak", "exposed", "stolen data", "compromised data",
        "ransomware attack", "data theft", "leaked credentials", "incident",
        "personal information", "customer data",
    ],
    "malware": [
        "malware", "ransomware", "trojan", "botnet", "infostealer", "rat",
        "banking malware", "loader", "backdoor", "stealer", "worm", "rootkit",
        "android malware", "linux malware", "macos malware",
    ],
    "ai_security": [
        "ai security", "llm", "prompt injection", "ai attack", "model security",
        "artificial intelligence", "generative ai", "chatgpt", "openai",
        "ai agent", "red team", "owasp llm", "ai vulnerability",
    ],
    "web_security": [
        "xss", "sql injection", "ssrf", "csrf", "web vulnerability", "api security",
        "authentication bypass", "owasp", "browser security", "web app",
        "injection", "cross-site",
    ],
    "cloud_security": [
        "aws", "azure", "google cloud", "gcp", "kubernetes", "container",
        "cloud security", "iam", "s3", "cloud breach", "misconfiguration",
    ],
    "mobile_security": [
        "android", "ios", "iphone", "mobile malware", "mobile security",
        "apk", "google play", "app store", "smartphone",
    ],
    "network_security": [
        "vpn", "router", "firewall", "dns", "wifi", "wi-fi", "network attack",
        "ddos", "bgp", "network security", "switch", "appliance",
    ],
    "bug_bounty": [
        "bug bounty", "disclosure", "responsible disclosure", "writeup",
        "hackerone", "bugcrowd", "vulnerability report", "researcher",
    ],
    "ctf": [
        "ctf", "capture the flag", "writeup", "challenge", "competition",
        "security research", "conference", "black hat", "defcon", "bsides",
    ],
    "tools": [
        "tool", "release", "open source", "github", "framework", "scanner",
        "utility", "new tool", "security tool",
    ],
}

# GitHub search for security tools (public API, rate limited but works unauthenticated)
GITHUB_SEARCH_TOOLS = "https://api.github.com/search/repositories?q=topic:cybersecurity+OR+topic:security-tools+OR+topic:penetration-testing&sort=updated&order=desc&per_page=15"

# HTTP defaults
USER_AGENT = "CyberPulse/1.0 (Termux; +https://github.com/cyberpulse)"
TIMEOUT = 15
MAX_ITEMS = 12
