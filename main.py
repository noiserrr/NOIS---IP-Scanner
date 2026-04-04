import shutil
import sys
import time
import os
import requests
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.align import Align
from rich.text import Text
from rich.live import Live
from rich import box

console = Console()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.clear()

def get_width():
    return shutil.get_terminal_size((80, 20)).columns

def center_obj(obj):
    return Align.center(obj)

def centered_input(prompt_text=""):
    width = get_width()
    full_prompt = f"{prompt_text} "
    padding = (width // 2) - (len(full_prompt) // 2)
    if padding < 0: padding = 0
    print("\n" + " " * padding, end="")
    return input(f"{prompt_text} ")

def draw_banner():
    console.clear()
    
    lines = [  # TEXT 'NOIS'
        "███╗   ██╗ ██████╗ ██╗███████╗",
        "████╗  ██║██╔═══██╗██║██╔════╝",
        "██╔██╗ ██║██║   ██║██║███████╗",
        "██║╚██╗██║██║   ██║██║╚════██║",
        "██║ ╚████║╚██████╔╝██║███████║",
        "╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝"
    ]

    banner_text = Text()
    for line in lines:
        banner_text.append(line[:23], style="bold red")
        banner_text.append(line[23:26], style="bold white")
        banner_text.append(line[26:], style="bold red")
        banner_text.append("\n")

    console.print(center_obj(banner_text))
    console.print(center_obj("[bold white]──────────────────────────────────────────[/bold white]"))
    console.print(center_obj("[bold white]PREMIUM IP INTELLIGENCE SYSTEM [bold red]v15.0[/bold red]"))
    console.print(center_obj("[bold white]──────────────────────────────────────────[/bold white]\n"))

def fetch_ip_data(ip):
    try:
        response = requests.get(f"https://ipwho.is/{ip}", timeout=10)
        if response.status_code == 200:
            r = response.json()
            if r.get("success"):
                return {
                    "IP ADDRESS": r.get("ip"),
                    "COUNTRY": f"{r.get('country')} ({r.get('country_code')})",
                    "CITY/REGION": f"{r.get('city')} / {r.get('region')}",
                    "ISP": r.get("connection", {}).get("isp"),
                    "ASN": f"AS{r.get('connection', {}).get('asn')}",
                    "COORDINATES": f"{r.get('latitude')}, {r.get('longitude')}",
                    "TYPE": r.get("type"),
                    "TIMESTAMP": datetime.now().strftime("%H:%M:%S")
                }
        return None
    except:
        return None

def show_result(data):
    draw_banner()
    if not data:
        console.print(center_obj("[bold red]✘ Failed to retrieve data![/bold red]"))
    else:
        table = Table(box=box.SIMPLE_HEAD, show_header=False, border_style="red")
        for k, v in data.items():
            table.add_row(f"[bold white]{k}[/bold white]", f": [bold red]{v}[/bold red]")

        console.print(center_obj(Panel(table, title="[bold white]ANALYSIS REPORT[/bold white]", border_style="red", expand=False, padding=(1, 4))))
    
    centered_input("Press Enter to return to menu...")

def main():
    while True:
        draw_banner()
        menu_items = (
            "[bold white][01][/bold white] [red]SCAN MY OWN IP[/red]\n"
            "[bold white][02][/bold white] [red]START TARGET ANALYSIS[/red]\n"
            "[bold white][03][/bold white] [red]BULK SCAN MODE[/red]\n"
            "[bold white][04][/bold white] [red]EXIT SYSTEM[/red]"
        )
        
        console.print(center_obj(Panel(menu_items, title="[bold white]COMMAND CENTER[/bold white]", border_style="red", padding=(1, 5), expand=False)))
        
        choice = centered_input("COMMAND:")

        if choice in ["1", "01"]:
            draw_banner()
            progress = Progress(SpinnerColumn(style="red"), TextColumn("[bold white]Gathering data..."), console=console, transient=True)
            with Live(center_obj(progress), console=console, transient=True):
                progress.add_task("", total=None)
                try:
                    my_ip = requests.get("https://api.ipify.org", timeout=5).text
                    data = fetch_ip_data(my_ip)
                except:
                    data = None
            show_result(data)
        
        elif choice in ["2", "02"]:
            target = centered_input("TARGET IP:")
            if target:
                draw_banner()
                progress = Progress(SpinnerColumn(style="red"), TextColumn("[bold red]Analyzing..."), console=console, transient=True)
                with Live(center_obj(progress), console=console, transient=True):
                    progress.add_task("", total=None)
                    data = fetch_ip_data(target)
                show_result(data)

        elif choice in ["3", "03"]:
            draw_banner()
            raw = centered_input("IP LIST (Comma separated):")
            if not raw: continue
            
            ips = [i.strip() for i in raw.split(",") if i.strip()]
            results = []
            
            progress = Progress(SpinnerColumn(style="red"), TextColumn("[bold white]Scanning List..."), console=console, transient=True)
            with Live(center_obj(progress), console=console, transient=True):
                task = progress.add_task("", total=len(ips))
                for ip in ips:
                    d = fetch_ip_data(ip)
                    if d: results.append(d)
                    progress.advance(task)
                    time.sleep(0.4)
            
            draw_banner()
            if results:
                table = Table(box=box.ROUNDED, border_style="red", title="[bold white]BULK RESULTS[/bold white]")
                table.add_column("IP ADDRESS", style="white")
                table.add_column("COUNTRY", style="red")
                table.add_column("ISP", style="white")
                for r in results:
                    table.add_row(r['IP ADDRESS'], r['COUNTRY'], r['ISP'])
                console.print(center_obj(table))
            else:
                console.print(center_obj("[bold red]No data found.[/bold red]"))
            
            centered_input("Press Enter to continue...")

        elif choice in ["4", "04"]:
            draw_banner()
            console.print(center_obj("[bold red]Shutting Down...[/bold red]"))
            time.sleep(1)
            clear_terminal()
            sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_terminal()
        sys.exit()
