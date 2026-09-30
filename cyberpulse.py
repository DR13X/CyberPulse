#!/usr/bin/env python3
"""
CyberPulse - Cybersecurity Intelligence CLI for Android Termux
Lightweight, rootless, terminal-only, live data only.

Run: python cyberpulse.py
"""

import sys

from ui import (
    clear_screen,
    print_main_menu,
    print_error,
    print_warning,
    print_info,
    print_success,
    wait_for_enter,
)
from news import check_internet, fetch_rss
from sources import NEWS_FEEDS

# Feature modules
from attacks import show_attacks
from breaches import show_breaches
from malware import show_malware
from tools import show_tools
from vulnerabilities import cve_menu
from research import (
    show_threat_intel,
    show_exploits,
    show_ai_security,
    show_web_security,
    show_cloud_security,
    show_mobile_security,
    show_network_security,
    show_bug_bounty,
    show_ctf_research,
)
from trends import show_trends, show_important_today
from ui import print_header, print_news_item, print_empty, loading


def show_news():
    print_header("LATEST CYBERSECURITY NEWS")
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return
    with loading("Fetching latest cybersecurity news..."):
        items = fetch_rss(NEWS_FEEDS, max_items=12)
    if not items:
        print_empty()
    else:
        for it in items:
            print_news_item(it)
    wait_for_enter()


def refresh_info():
    print_header("REFRESH")
    print_info("Re-checking connectivity and sample feeds...")
    if not check_internet():
        print_error("Internet connection unavailable.")
    else:
        print_success("Internet connection OK.")
        with loading("Probing primary news sources..."):
            items = fetch_rss(NEWS_FEEDS[:3], max_items=3)
        if items:
            print_success(f"Live data available ({len(items)} sample items retrieved).")
        else:
            print_warning("Connectivity OK but some sources returned no items.")
    wait_for_enter()


def main():
    while True:
        try:
            clear_screen()
            print_main_menu()
            choice = input().strip()
        except (EOFError, KeyboardInterrupt):
            print()
            print_info("Exiting CyberPulse. Stay safe.")
            sys.exit(0)

        if choice == "0":
            print_info("Exiting CyberPulse. Stay safe.")
            sys.exit(0)
        elif choice == "1":
            show_news()
        elif choice == "2":
            show_attacks()
        elif choice == "3":
            show_exploits()
        elif choice == "4":
            cve_menu()
        elif choice == "5":
            show_breaches()
        elif choice == "6":
            show_malware()
        elif choice == "7":
            show_tools()
        elif choice == "8":
            show_threat_intel()
        elif choice == "9":
            show_ai_security()
        elif choice == "10":
            show_web_security()
        elif choice == "11":
            show_cloud_security()
        elif choice == "12":
            show_mobile_security()
        elif choice == "13":
            show_network_security()
        elif choice == "14":
            show_bug_bounty()
        elif choice == "15":
            show_ctf_research()
        elif choice == "16":
            show_trends()
        elif choice == "17":
            show_important_today()
        elif choice == "18":
            refresh_info()
        else:
            print_warning("Invalid option. Enter a number from the menu.")
            wait_for_enter()


if __name__ == "__main__":
    main()
