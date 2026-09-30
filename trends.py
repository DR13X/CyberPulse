"""
CyberPulse - Trends and daily briefing.
Based only on live-fetched items (temporary in memory).
"""

from collections import Counter
from typing import List, Dict

from news import fetch_rss, check_internet
from sources import (
    NEWS_FEEDS,
    ATTACK_FEEDS,
    MALWARE_FEEDS,
    THREAT_INTEL_FEEDS,
    AI_SECURITY_FEEDS,
    BREACH_FEEDS,
    KEYWORDS,
)
from ui import (
    print_header,
    print_trends,
    print_briefing,
    print_empty,
    print_error,
    print_info,
    loading,
    wait_for_enter,
)


# Topic buckets used for trend detection
TREND_TOPICS = {
    "AI Security": KEYWORDS["ai_security"],
    "Ransomware": ["ransomware", "extortion", "encrypt"],
    "Cloud Security": KEYWORDS["cloud_security"],
    "Supply Chain Attacks": ["supply chain", "supply-chain", "third-party", "dependency"],
    "Identity Security": ["identity", "credential", "mfa", "sso", "authentication", "account takeover"],
    "Zero-Day / Exploits": KEYWORDS["exploits"] + ["zero-day", "0-day"],
    "Data Breaches": KEYWORDS["breaches"],
    "Malware": KEYWORDS["malware"],
    "Mobile Security": KEYWORDS["mobile_security"],
    "Web Security": KEYWORDS["web_security"],
    "APT / Espionage": ["apt", "espionage", "nation-state", "threat actor"],
    "Phishing": ["phishing", "credential harvesting", "smishing"],
}


def _gather_headlines(max_per_source_group: int = 8) -> List[Dict]:
    """Fetch a broad set of recent headlines for analysis."""
    all_items = []
    groups = [
        NEWS_FEEDS[:4],
        ATTACK_FEEDS[:3],
        MALWARE_FEEDS[:3],
        BREACH_FEEDS[:2],
        AI_SECURITY_FEEDS[:2],
        THREAT_INTEL_FEEDS[:2],
    ]
    for feeds in groups:
        items = fetch_rss(feeds, max_items=max_per_source_group)
        all_items.extend(items)
    # Dedupe by title
    seen = set()
    unique = []
    for it in all_items:
        t = it.get("title", "").lower()
        if t and t not in seen:
            seen.add(t)
            unique.append(it)
    return unique


def show_trends():
    print_header("CYBERSECURITY TRENDS")
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return

    with loading("Analyzing current cybersecurity topics..."):
        items = _gather_headlines()

    if not items:
        print_empty()
        wait_for_enter()
        return

    scores = Counter()
    examples = {k: [] for k in TREND_TOPICS}

    for it in items:
        blob = (it.get("title", "") + " " + it.get("summary", "")).lower()
        for topic, kws in TREND_TOPICS.items():
            if any(kw.lower() in blob for kw in kws):
                scores[topic] += 1
                if len(examples[topic]) < 2:
                    examples[topic].append(it.get("title", "")[:80])

    if not scores:
        print_info("Could not detect strong recurring themes from current feeds.")
        wait_for_enter()
        return

    ranked = scores.most_common(7)
    trends = []
    for name, count in ranked:
        reason_parts = [f"Appeared in ~{count} recent headlines."]
        if examples[name]:
            reason_parts.append(f"Example: \"{examples[name][0]}\"")
        trends.append({
            "name": name,
            "reason": " ".join(reason_parts),
        })

    print_trends(trends)
    wait_for_enter()


def show_important_today():
    print_header("WHAT'S IMPORTANT TODAY")
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return

    sections = {
        "CRITICAL": [],
        "ATTACKS": [],
        "BREACHES": [],
        "MALWARE": [],
        "TOOLS": [],
        "AI SECURITY": [],
        "TREND": [],
    }

    with loading("Building today's cybersecurity briefing..."):
        # Critical / CVE-ish
        from sources import CVE_FEEDS
        cves = fetch_rss(CVE_FEEDS[:3], max_items=5)
        for it in cves[:2]:
            title = it.get("title", "")
            if any(x in title.lower() for x in ("critical", "actively exploited", "kev", "zero-day")):
                sections["CRITICAL"].append(title[:100])
        if not sections["CRITICAL"] and cves:
            sections["CRITICAL"].append(cves[0].get("title", "")[:100])

        attacks = fetch_rss(ATTACK_FEEDS[:3], keywords=KEYWORDS["attacks"], max_items=5)
        for it in attacks[:2]:
            sections["ATTACKS"].append(it.get("title", "")[:100])

        breaches = fetch_rss(BREACH_FEEDS[:3], keywords=KEYWORDS["breaches"], max_items=5)
        for it in breaches[:2]:
            sections["BREACHES"].append(it.get("title", "")[:100])

        malware = fetch_rss(MALWARE_FEEDS[:3], keywords=KEYWORDS["malware"], max_items=5)
        for it in malware[:2]:
            sections["MALWARE"].append(it.get("title", "")[:100])

        tools = fetch_rss(NEWS_FEEDS[:3], keywords=KEYWORDS["tools"], max_items=4)
        for it in tools[:1]:
            sections["TOOLS"].append(it.get("title", "")[:100])

        ai = fetch_rss(AI_SECURITY_FEEDS[:3], keywords=KEYWORDS["ai_security"], max_items=4)
        for it in ai[:2]:
            sections["AI SECURITY"].append(it.get("title", "")[:100])

        # Simple trend hint from counts
        all_titles = " ".join(
            it.get("title", "") for group in (attacks, breaches, malware, ai, cves) for it in group
        ).lower()
        trend_hits = []
        for topic, kws in TREND_TOPICS.items():
            if sum(1 for kw in kws if kw.lower() in all_titles) >= 2:
                trend_hits.append(topic)
        if trend_hits:
            sections["TREND"].append(", ".join(trend_hits[:3]))
        else:
            sections["TREND"].append("Mixed topics — check Trends menu for detail")

    # Drop empty sections for cleaner output
    clean = {k: v for k, v in sections.items() if v}
    if not clean:
        print_empty()
    else:
        print_briefing(clean)
    wait_for_enter()
