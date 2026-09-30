"""
CyberPulse - Live RSS / HTTP fetch helpers.
No caching, no storage. All data is temporary in memory.
"""

import re
import html
from datetime import datetime
from email.utils import parsedate_to_datetime
from typing import List, Dict, Optional, Callable

import requests
import feedparser
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from sources import USER_AGENT, TIMEOUT, MAX_ITEMS
from ui import print_error, print_warning, print_info

# Shared session with retries
_session = None


def get_session() -> requests.Session:
    global _session
    if _session is None:
        _session = requests.Session()
        _session.headers.update({
            "User-Agent": USER_AGENT,
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, application/json, */*",
        })
        retry = Retry(
            total=2,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "HEAD"],
        )
        adapter = HTTPAdapter(max_retries=retry)
        _session.mount("https://", adapter)
        _session.mount("http://", adapter)
    return _session


def check_internet() -> bool:
    """Quick connectivity check."""
    try:
        r = get_session().get("https://www.google.com", timeout=5)
        return r.status_code < 500
    except Exception:
        try:
            r = get_session().get("https://1.1.1.1", timeout=5)
            return True
        except Exception:
            return False


def clean_html(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_date(entry) -> str:
    """Extract a human-readable date from a feed entry."""
    for attr in ("published", "updated", "created"):
        val = getattr(entry, attr, None) or entry.get(attr)
        if val:
            try:
                dt = parsedate_to_datetime(val)
                return dt.strftime("%Y-%m-%d %H:%M UTC")
            except Exception:
                try:
                    # feedparser sometimes provides structured time
                    st = getattr(entry, f"{attr}_parsed", None)
                    if st:
                        dt = datetime(*st[:6])
                        return dt.strftime("%Y-%m-%d %H:%M UTC")
                except Exception:
                    pass
            return str(val)[:30]
    return "N/A"


def fetch_rss(
    feeds: List[Dict],
    keywords: Optional[List[str]] = None,
    max_items: int = MAX_ITEMS,
    filter_fn: Optional[Callable] = None,
) -> List[Dict]:
    """
    Fetch multiple RSS feeds, merge, optionally filter by keywords,
    sort by date (best-effort), return up to max_items unique items.
    Never raises — individual feed failures are reported and skipped.
    """
    results = []
    seen_titles = set()
    session = get_session()

    for feed in feeds:
        name = feed.get("name", "Unknown")
        url = feed.get("url", "")
        category = feed.get("category", "General")
        try:
            resp = session.get(url, timeout=TIMEOUT)
            if resp.status_code != 200:
                print_warning(f"Source unavailable: {name} (HTTP {resp.status_code})")
                continue
            parsed = feedparser.parse(resp.content)
            if getattr(parsed, "bozo", False) and not parsed.entries:
                print_warning(f"Source unavailable: {name} (invalid RSS)")
                continue
            for entry in parsed.entries:
                title = clean_html(getattr(entry, "title", "") or entry.get("title", ""))
                if not title or title.lower() in seen_titles:
                    continue
                summary = clean_html(
                    getattr(entry, "summary", "")
                    or entry.get("summary", "")
                    or getattr(entry, "description", "")
                    or entry.get("description", "")
                )
                link = getattr(entry, "link", "") or entry.get("link", "")
                published = parse_date(entry)

                item = {
                    "title": title,
                    "source": name,
                    "published": published,
                    "category": category,
                    "summary": summary,
                    "url": link,
                    "raw": entry,
                }

                # Keyword filter (case-insensitive on title+summary)
                if keywords:
                    blob = (title + " " + summary).lower()
                    if not any(kw.lower() in blob for kw in keywords):
                        continue

                if filter_fn and not filter_fn(item):
                    continue

                seen_titles.add(title.lower())
                results.append(item)
        except requests.exceptions.Timeout:
            print_warning(f"Source unavailable: {name} (timeout)")
        except requests.exceptions.ConnectionError:
            print_warning(f"Source unavailable: {name} (connection error)")
        except Exception as e:
            print_warning(f"Source unavailable: {name} ({type(e).__name__})")

    # Best-effort sort: prefer items with real dates
    def sort_key(it):
        p = it.get("published", "")
        if p and p != "N/A":
            return p
        return "0000"

    results.sort(key=sort_key, reverse=True)
    return results[:max_items]


def fetch_json(url: str, source_name: str = "API") -> Optional[dict]:
    """Fetch JSON from a public API. Returns None on failure."""
    try:
        resp = get_session().get(url, timeout=TIMEOUT)
        if resp.status_code != 200:
            print_warning(f"Source unavailable: {source_name} (HTTP {resp.status_code})")
            return None
        return resp.json()
    except requests.exceptions.Timeout:
        print_warning(f"Source unavailable: {source_name} (timeout)")
    except requests.exceptions.ConnectionError:
        print_warning(f"Source unavailable: {source_name} (connection error)")
    except Exception as e:
        print_warning(f"Source unavailable: {source_name} ({type(e).__name__})")
    return None


def extract_cve_id(text: str) -> Optional[str]:
    m = re.search(r"CVE-\d{4}-\d{4,}", text or "", re.IGNORECASE)
    return m.group(0).upper() if m else None


def severity_from_text(text: str) -> str:
    t = (text or "").lower()
    if "critical" in t:
        return "CRITICAL"
    if "high" in t:
        return "HIGH"
    if "medium" in t or "moderate" in t:
        return "MEDIUM"
    if "low" in t:
        return "LOW"
    return "N/A"
