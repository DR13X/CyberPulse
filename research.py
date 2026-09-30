"""
CyberPulse - Topic modules: threat intel, AI, web, cloud, mobile, network,
bug bounty, CTF/research.
"""

from news import fetch_rss, check_internet
from sources import (
    THREAT_INTEL_FEEDS,
    AI_SECURITY_FEEDS,
    WEB_SECURITY_FEEDS,
    CLOUD_SECURITY_FEEDS,
    MOBILE_SECURITY_FEEDS,
    NETWORK_SECURITY_FEEDS,
    BUG_BOUNTY_FEEDS,
    CTF_RESEARCH_FEEDS,
    EXPLOIT_FEEDS,
    KEYWORDS,
)
from ui import (
    print_header,
    print_news_item,
    print_empty,
    print_error,
    loading,
    wait_for_enter,
)


def _show_topic(title: str, feeds, keywords=None, default_category="General"):
    print_header(title)
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return
    with loading(f"Fetching {title.lower()}..."):
        items = fetch_rss(feeds, keywords=keywords, max_items=12)
    if not items and keywords:
        items = fetch_rss(feeds, max_items=10)
    if not items:
        print_empty()
    else:
        for it in items:
            if not it.get("category") or it["category"] == "General":
                it["category"] = default_category
            print_news_item(it)
    wait_for_enter()


def show_threat_intel():
    _show_topic(
        "THREAT INTELLIGENCE",
        THREAT_INTEL_FEEDS,
        keywords=None,
        default_category="Threat Intelligence",
    )


def show_exploits():
    print_header("EXPLOITS & PoC NEWS")
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return
    with loading("Fetching exploit and PoC related news..."):
        items = fetch_rss(
            EXPLOIT_FEEDS,
            keywords=KEYWORDS["exploits"],
            max_items=12,
        )
    if not items:
        items = fetch_rss(EXPLOIT_FEEDS, max_items=10)
    if not items:
        print_empty()
    else:
        for it in items:
            # Enrich display fields where possible
            from news import extract_cve_id, severity_from_text
            title = it.get("title", "")
            summary = it.get("summary", "")
            cve = extract_cve_id(title) or extract_cve_id(summary)
            sev = severity_from_text(title + " " + summary)
            extra = []
            if cve:
                extra.append(f"CVE: {cve}")
            if sev != "N/A":
                extra.append(f"Severity: {sev}")
            if extra:
                it["category"] = " | ".join(extra)
            else:
                it["category"] = "Exploit / PoC"
            print_news_item(it)
    wait_for_enter()


def show_ai_security():
    _show_topic(
        "AI SECURITY",
        AI_SECURITY_FEEDS,
        keywords=KEYWORDS["ai_security"],
        default_category="AI Security",
    )


def show_web_security():
    _show_topic(
        "WEB SECURITY",
        WEB_SECURITY_FEEDS,
        keywords=KEYWORDS["web_security"],
        default_category="Web Security",
    )


def show_cloud_security():
    _show_topic(
        "CLOUD SECURITY",
        CLOUD_SECURITY_FEEDS,
        keywords=KEYWORDS["cloud_security"],
        default_category="Cloud Security",
    )


def show_mobile_security():
    _show_topic(
        "MOBILE SECURITY",
        MOBILE_SECURITY_FEEDS,
        keywords=KEYWORDS["mobile_security"],
        default_category="Mobile Security",
    )


def show_network_security():
    _show_topic(
        "NETWORK SECURITY",
        NETWORK_SECURITY_FEEDS,
        keywords=KEYWORDS["network_security"],
        default_category="Network Security",
    )


def show_bug_bounty():
    _show_topic(
        "BUG BOUNTY & DISCLOSURES",
        BUG_BOUNTY_FEEDS,
        keywords=KEYWORDS["bug_bounty"],
        default_category="Bug Bounty",
    )


def show_ctf_research():
    _show_topic(
        "CTF & SECURITY RESEARCH",
        CTF_RESEARCH_FEEDS,
        keywords=KEYWORDS["ctf"],
        default_category="CTF / Research",
    )
