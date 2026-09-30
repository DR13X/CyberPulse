"""
CyberPulse - Cyber attacks module.
"""

from news import fetch_rss, check_internet
from sources import ATTACK_FEEDS, KEYWORDS
from ui import (
    print_header,
    print_news_item,
    print_empty,
    print_error,
    loading,
    wait_for_enter,
)


def show_attacks():
    print_header("LATEST CYBER ATTACKS")
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return
    with loading("Fetching recent cyber attack reports..."):
        items = fetch_rss(
            ATTACK_FEEDS,
            keywords=KEYWORDS["attacks"],
            max_items=12,
        )
    if not items:
        # Broader fallback without strict keyword filter
        items = fetch_rss(ATTACK_FEEDS, max_items=10)
    if not items:
        print_empty()
    else:
        for it in items:
            # Tag likely attack types from title/summary
            blob = (it.get("title", "") + " " + it.get("summary", "")).lower()
            tags = []
            for t in (
                "ransomware", "phishing", "ddos", "supply-chain", "espionage",
                "infrastructure", "account", "cloud", "web attack", "apt",
            ):
                if t in blob:
                    tags.append(t)
            if tags:
                it["category"] = " / ".join(tags[:3]).title()
            else:
                it["category"] = "Cyber Attack"
            print_news_item(it)
    wait_for_enter()
