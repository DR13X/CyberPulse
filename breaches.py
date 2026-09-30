"""
CyberPulse - Data breaches module.
"""

from news import fetch_rss, check_internet, clean_html
from sources import BREACH_FEEDS, KEYWORDS
from ui import (
    print_header,
    print_breach_item,
    print_empty,
    print_error,
    loading,
    wait_for_enter,
)


def show_breaches():
    print_header("DATA BREACHES & SECURITY INCIDENTS")
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return
    with loading("Fetching recent data breach reports..."):
        items = fetch_rss(
            BREACH_FEEDS,
            keywords=KEYWORDS["breaches"],
            max_items=12,
        )
    if not items:
        items = fetch_rss(BREACH_FEEDS, max_items=10)

    if not items:
        print_empty()
        wait_for_enter()
        return

    for it in items:
        title = it.get("title", "")
        summary = it.get("summary", "")
        # Heuristic organization name from title
        org = "See report"
        for sep in (" - ", " – ", ": ", " | "):
            if sep in title:
                org = title.split(sep)[0].strip()[:80]
                break
        blob = (title + " " + summary).lower()
        itype = "Reported incident"
        if "ransomware" in blob:
            itype = "Ransomware / extortion"
        elif "leak" in blob or "exposed" in blob:
            itype = "Data exposure / leak"
        elif "breach" in blob:
            itype = "Data breach"
        elif "phish" in blob:
            itype = "Phishing-related incident"

        print_breach_item({
            "title": title,
            "organization": org,
            "incident": summary[:250] if summary else title,
            "published": it.get("published", "N/A"),
            "type": itype,
            "data_affected": "See original report for details",
            "source": it.get("source", "N/A"),
            "url": it.get("url", ""),
            "note": "Publicly reported. Confirm details from primary sources.",
        })
    wait_for_enter()
