"""
CyberPulse - CVE / Vulnerability modules.
Live fetch only. No storage.
"""

from typing import List, Dict

from news import fetch_rss, fetch_json, extract_cve_id, severity_from_text, clean_html
from sources import CVE_FEEDS, CISA_KEV_JSON, KEYWORDS
from ui import (
    print_header,
    print_cve_item,
    print_cve_submenu,
    print_empty,
    print_error,
    print_info,
    print_warning,
    loading,
    wait_for_enter,
)
from news import check_internet


def _rss_to_cve_items(items: List[Dict], severity_filter: str = None) -> List[Dict]:
    out = []
    for it in items:
        title = it.get("title", "")
        summary = it.get("summary", "")
        cve_id = extract_cve_id(title) or extract_cve_id(summary) or "See title"
        sev = severity_from_text(title + " " + summary)
        if severity_filter:
            if severity_filter == "CRITICAL" and sev != "CRITICAL":
                continue
            if severity_filter == "HIGH" and sev not in ("HIGH", "CRITICAL"):
                continue
        out.append({
            "cve_id": cve_id if cve_id != "See title" else title[:60],
            "title": title,
            "severity": sev,
            "cvss": "",
            "product": "",
            "description": summary[:400] if summary else title,
            "published": it.get("published", "N/A"),
            "exploitation": "Unknown / check source",
            "source": it.get("source", "N/A"),
            "url": it.get("url", ""),
        })
    return out


def show_latest_cves():
    print_header("LATEST CVEs")
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return
    with loading("Fetching latest CVEs..."):
        items = fetch_rss(CVE_FEEDS, max_items=15)
    cves = _rss_to_cve_items(items)
    if not cves:
        print_empty()
    else:
        for c in cves[:12]:
            print_cve_item(c)
    wait_for_enter()


def show_critical_cves():
    print_header("CRITICAL CVEs")
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return
    with loading("Fetching critical CVEs..."):
        items = fetch_rss(CVE_FEEDS, max_items=20)
    cves = _rss_to_cve_items(items, severity_filter="CRITICAL")
    if not cves:
        # Fallback: show high+critical keyword matches
        items2 = fetch_rss(
            CVE_FEEDS,
            keywords=["critical", "cvss 9", "cvss 10", "severity: critical"],
            max_items=12,
        )
        cves = _rss_to_cve_items(items2)
    if not cves:
        print_empty()
    else:
        for c in cves[:10]:
            print_cve_item(c)
    wait_for_enter()


def show_high_cves():
    print_header("HIGH SEVERITY CVEs")
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return
    with loading("Fetching high severity CVEs..."):
        items = fetch_rss(CVE_FEEDS, max_items=20)
    cves = _rss_to_cve_items(items, severity_filter="HIGH")
    if not cves:
        items2 = fetch_rss(
            CVE_FEEDS,
            keywords=["high", "critical", "severity"],
            max_items=12,
        )
        cves = _rss_to_cve_items(items2)
    if not cves:
        print_empty()
    else:
        for c in cves[:10]:
            print_cve_item(c)
    wait_for_enter()


def show_cisa_kev():
    print_header("CISA KNOWN EXPLOITED VULNERABILITIES (KEV)")
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return
    with loading("Fetching CISA KEV catalog..."):
        data = fetch_json(CISA_KEV_JSON, "CISA KEV")
    if not data or "vulnerabilities" not in data:
        # Fallback to alerts RSS
        print_warning("KEV JSON unavailable, trying CISA Alerts RSS...")
        from sources import CVE_FEEDS
        alerts = [f for f in CVE_FEEDS if "Alerts" in f["name"] or "CISA" in f["name"]]
        items = fetch_rss(alerts, max_items=12)
        cves = _rss_to_cve_items(items)
        for c in cves:
            c["exploitation"] = "Listed / referenced by CISA"
            print_cve_item(c)
        if not cves:
            print_empty()
        wait_for_enter()
        return

    vulns = data.get("vulnerabilities", [])
    # Sort by dateAdded descending
    try:
        vulns = sorted(vulns, key=lambda x: x.get("dateAdded", ""), reverse=True)
    except Exception:
        pass

    count = 0
    for v in vulns:
        if count >= 12:
            break
        cve_id = v.get("cveID", "N/A")
        name = v.get("vulnerabilityName", "")
        desc = v.get("shortDescription", "")
        product = f"{v.get('vendorProject', '')} {v.get('product', '')}".strip()
        date_added = v.get("dateAdded", "N/A")
        required = v.get("requiredAction", "")
        item = {
            "cve_id": cve_id,
            "severity": "KNOWN EXPLOITED",
            "cvss": "",
            "product": product or name,
            "description": desc or name,
            "published": date_added,
            "exploitation": f"CISA KEV — {required}" if required else "Actively exploited (CISA KEV)",
            "source": "CISA KEV Catalog",
            "url": f"https://nvd.nist.gov/vuln/detail/{cve_id}" if cve_id.startswith("CVE-") else "https://www.cisa.gov/known-exploited-vulnerabilities-catalog",
        }
        print_cve_item(item)
        count += 1

    if count == 0:
        print_empty()
    wait_for_enter()


def cve_menu():
    while True:
        print_cve_submenu()
        try:
            choice = input().strip()
        except (EOFError, KeyboardInterrupt):
            return
        if choice == "1":
            show_latest_cves()
        elif choice == "2":
            show_critical_cves()
        elif choice == "3":
            show_high_cves()
        elif choice == "4":
            show_cisa_kev()
        elif choice == "5" or choice == "0":
            return
        else:
            print_warning("Invalid option.")
