"""
CyberPulse - Terminal UI helpers using Rich.
No Textual, no TUI framework — pure print + input.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box
from rich.rule import Rule
from rich.status import Status
import time

console = Console()


def clear_screen():
    console.clear()


def print_banner():
    banner = Text()
    banner.append("=" * 60 + "\n", style="cyan")
    banner.append("                 CYBERPULSE\n", style="bold cyan")
    banner.append("          CYBERSECURITY INTELLIGENCE\n", style="bold white")
    banner.append("              TERMUX EDITION\n", style="green")
    banner.append("=" * 60, style="cyan")
    console.print(banner)


def print_main_menu():
    print_banner()
    menu = """
[1]  Latest Cybersecurity News
[2]  Latest Cyber Attacks
[3]  Exploits & PoC News
[4]  Latest Vulnerabilities / CVEs
[5]  Data Breaches
[6]  Malware & Ransomware
[7]  New Cybersecurity Tools
[8]  Threat Intelligence
[9]  AI Security
[10] Web Security
[11] Cloud Security
[12] Mobile Security
[13] Network Security
[14] Bug Bounty & Disclosures
[15] CTF & Security Research
[16] Cybersecurity Trends
[17] What's Important Today
[18] Refresh
[0]  Exit
"""
    console.print(menu, style="white")
    console.print("Select option: ", style="bold yellow", end="")


def print_header(title: str):
    console.print()
    console.print(Rule(f"[bold cyan]{title}[/bold cyan]", style="cyan"))
    console.print()


def print_item_separator():
    console.print("-" * 60, style="dim")


def print_news_item(item: dict):
    """Standard news-style item display."""
    print_item_separator()
    console.print(f"[bold white]{item.get('title', 'No title')}[/bold white]")
    console.print(f"[cyan]Source:[/cyan]  {item.get('source', 'Unknown')}")
    console.print(f"[cyan]Published:[/cyan]  {item.get('published', 'N/A')}")
    console.print(f"[cyan]Category:[/cyan]  {item.get('category', 'General')}")
    summary = item.get("summary", "")
    if summary:
        # Truncate long summaries
        if len(summary) > 280:
            summary = summary[:277] + "..."
        console.print(f"[cyan]Summary:[/cyan]  {summary}")
    url = item.get("url", "")
    if url:
        console.print(f"[cyan]URL:[/cyan]  [link={url}]{url}[/link]")
    print_item_separator()


def print_cve_item(item: dict):
    print_item_separator()
    console.print(f"[bold red]{item.get('cve_id', item.get('title', 'CVE'))}[/bold red]")
    console.print(f"[cyan]Severity:[/cyan]  {item.get('severity', 'N/A')}")
    if item.get("cvss"):
        console.print(f"[cyan]CVSS:[/cyan]  {item.get('cvss')}")
    if item.get("product"):
        console.print(f"[cyan]Affected:[/cyan]  {item.get('product')}")
    if item.get("description"):
        desc = item["description"]
        if len(desc) > 300:
            desc = desc[:297] + "..."
        console.print(f"[cyan]Description:[/cyan]  {desc}")
    console.print(f"[cyan]Published:[/cyan]  {item.get('published', 'N/A')}")
    if item.get("exploitation"):
        console.print(f"[cyan]Exploitation:[/cyan]  {item.get('exploitation')}")
    console.print(f"[cyan]Source:[/cyan]  {item.get('source', 'N/A')}")
    if item.get("url"):
        console.print(f"[cyan]URL:[/cyan]  [link={item['url']}]{item['url']}[/link]")
    print_item_separator()


def print_breach_item(item: dict):
    print_item_separator()
    console.print(f"[bold yellow]{item.get('title', 'Breach Report')}[/bold yellow]")
    console.print(f"[cyan]Organization:[/cyan]  {item.get('organization', 'See report')}")
    console.print(f"[cyan]Incident:[/cyan]  {item.get('incident', item.get('summary', 'N/A')[:200])}")
    console.print(f"[cyan]Date:[/cyan]  {item.get('published', 'N/A')}")
    console.print(f"[cyan]Type:[/cyan]  {item.get('type', 'Reported incident')}")
    if item.get("data_affected"):
        console.print(f"[cyan]Data affected:[/cyan]  {item.get('data_affected')}")
    console.print(f"[cyan]Source:[/cyan]  {item.get('source', 'N/A')}")
    note = item.get("note", "Publicly reported — verify independently.")
    console.print(f"[dim]Note: {note}[/dim]")
    if item.get("url"):
        console.print(f"[cyan]URL:[/cyan]  [link={item['url']}]{item['url']}[/link]")
    print_item_separator()


def print_tool_item(item: dict):
    print_item_separator()
    console.print(f"[bold green]{item.get('name', 'Tool')}[/bold green]")
    if item.get("description"):
        desc = item["description"]
        if len(desc) > 250:
            desc = desc[:247] + "..."
        console.print(f"[cyan]Description:[/cyan]  {desc}")
    console.print(f"[cyan]Developer:[/cyan]  {item.get('developer', 'N/A')}")
    console.print(f"[cyan]Latest:[/cyan]  {item.get('updated', 'N/A')}")
    if item.get("language"):
        console.print(f"[cyan]Language:[/cyan]  {item.get('language')}")
    if item.get("stars") is not None:
        console.print(f"[cyan]Stars:[/cyan]  {item.get('stars')}")
    if item.get("url"):
        console.print(f"[cyan]GitHub:[/cyan]  [link={item['url']}]{item['url']}[/link]")
    print_item_separator()


def print_error(msg: str):
    console.print(f"[bold red][!] {msg}[/bold red]")


def print_warning(msg: str):
    console.print(f"[bold yellow][!] {msg}[/bold yellow]")


def print_info(msg: str):
    console.print(f"[cyan][*] {msg}[/cyan]")


def print_success(msg: str):
    console.print(f"[green][+] {msg}[/green]")


def loading(message: str = "Fetching live data..."):
    return Status(f"[bold cyan]{message}[/bold cyan]", console=console, spinner="dots")


def wait_for_enter():
    console.print()
    console.print("[dim][Enter] Return to Main Menu[/dim]")
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        pass


def print_empty():
    console.print("[yellow]No results found from available sources at this time.[/yellow]")


def print_trends(trends: list):
    print_header("CYBERSECURITY TRENDS")
    if not trends:
        print_empty()
        return
    for i, t in enumerate(trends, 1):
        console.print(f"[bold cyan][{i}] {t['name']}[/bold cyan]")
        console.print(f"    {t['reason']}")
        console.print()


def print_briefing(sections: dict):
    print_header("WHAT'S IMPORTANT TODAY")
    order = [
        ("CRITICAL", "bold red"),
        ("ATTACKS", "bold yellow"),
        ("BREACHES", "bold yellow"),
        ("MALWARE", "bold magenta"),
        ("TOOLS", "bold green"),
        ("AI SECURITY", "bold blue"),
        ("TREND", "bold cyan"),
    ]
    for key, style in order:
        items = sections.get(key, [])
        if items:
            console.print(f"[{style}]{key}[/{style}]")
            for it in items:
                console.print(f"  - {it}")
            console.print()
    console.print("=" * 60, style="cyan")


def print_cve_submenu():
    console.print()
    console.print("[bold]CVE Submenu[/bold]")
    console.print("[1] Latest CVEs")
    console.print("[2] Critical CVEs")
    console.print("[3] High Severity CVEs")
    console.print("[4] CISA KEV")
    console.print("[5] Back")
    console.print("Select option: ", style="bold yellow", end="")
