"""
CyberPulse - New cybersecurity tools (GitHub + RSS).
Does NOT download or execute any tools.
"""

from news import fetch_rss, fetch_json, check_internet, clean_html
from sources import GITHUB_SEARCH_TOOLS, NEWS_FEEDS, KEYWORDS
from ui import (
    print_header,
    print_tool_item,
    print_news_item,
    print_empty,
    print_error,
    print_info,
    loading,
    wait_for_enter,
)


def show_tools():
    print_header("NEW CYBERSECURITY TOOLS")
    if not check_internet():
        print_error("Internet connection unavailable.")
        wait_for_enter()
        return

    tools_found = []

    with loading("Fetching recent security tools from GitHub..."):
        data = fetch_json(GITHUB_SEARCH_TOOLS, "GitHub Search")

    if data and "items" in data:
        for repo in data["items"][:12]:
            tools_found.append({
                "name": repo.get("full_name") or repo.get("name", "Unknown"),
                "description": repo.get("description") or "No description",
                "developer": (repo.get("owner") or {}).get("login", "N/A"),
                "updated": (repo.get("updated_at") or "")[:10],
                "language": repo.get("language") or "N/A",
                "stars": repo.get("stargazers_count"),
                "url": repo.get("html_url", ""),
            })

    # Also pull tool-related news
    with loading("Fetching tool release news..."):
        news_items = fetch_rss(
            NEWS_FEEDS[:5],
            keywords=KEYWORDS["tools"] + ["github", "open-source", "released"],
            max_items=6,
        )

    if tools_found:
        print_info(f"Showing {len(tools_found)} recently updated security-related repositories:")
        for t in tools_found:
            print_tool_item(t)
    else:
        print_info("GitHub search unavailable or rate-limited; showing news only.")

    if news_items:
        print_info("Related tool / release news:")
        for it in news_items:
            it["category"] = "Tool / Release"
            print_news_item(it)

    if not tools_found and not news_items:
        print_empty()

    wait_for_enter()
