import time
import msvcrt
from collections import deque

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
from rich.layout import Layout
from rich.align import Align
from rich.text import Text

from backend.services.system_stat import get_system_stats
from backend.services.process_manager import get_top_processes, kill_process

console = Console()

cpu_history = deque(maxlen=50)
current_sort = "cpu"
running = True
selected_index = 0
last_process_fetch = 0
cached_processes = []



def get_color(value):
    if value < 40:
        return "green"
    elif value < 70:
        return "yellow"
    else:
        return "red"


def get_bar(value):
    blocks = int(value // 5)
    return "█" * blocks + "░" * (20 - blocks)


def get_cpu_graph(value):
    cpu_history.append(value)

    graph = ""
    for v in cpu_history:
        level = int(v // 5)
        graph += "▁▂▃▄▅▆▇█"[min(level, 7)]

    return graph


def get_system_mood(cpu):
    if cpu < 30:
        return "Idle"
    elif cpu < 70:
        return "Busy"
    else:
        return "Overloaded"


def get_kill_recommendation(processes):
    if not processes:
        return "No processes"

    top = max(processes, key=lambda x: x["cpu_percent"])

    if top["cpu_percent"] > 50:
        return f"Kill {top['name']} (PID {top['pid']}) using {top['cpu_percent']:.1f}% CPU"
    else:
        return "No critical process detected"



def generate_dashboard():
    global selected_index, last_process_fetch, cached_processes

    layout = Layout()

    layout.split(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=6)
    )

    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="right")
    )

    layout["left"].split_column(
        Layout(name="stats"),
        Layout(name="graph")
    )

    
    layout["header"].update(
        Panel(Align.center(" SMART PROCESS MONITOR "), style="bold cyan")
    )

    
    stats = get_system_stats()
    cpu = stats["cpu"]["total_cpu_percent"]
    memory = stats["memory"]["percent"]
    disk = stats["disk"]["percent"]

    stats_text = Text()
    stats_text.append(f"CPU: {get_bar(cpu)} {cpu:.2f}%\n", style=get_color(cpu))
    stats_text.append(f"Memory: {get_bar(memory)} {memory:.2f}%\n", style=get_color(memory))
    stats_text.append(f"Disk: {get_bar(disk)} {disk:.2f}%", style=get_color(disk))

    layout["stats"].update(
        Panel(stats_text, title=" Stats", border_style="cyan")
    )


    graph = get_cpu_graph(cpu)

    layout["graph"].update(
        Panel(
            f"{graph}\n\nCPU Usage Over Time",
            title=" CPU Graph",
            border_style="green"
        )
    )

    
    current_time = time.time()

    if current_time - last_process_fetch > 1:
        cached_processes = get_top_processes(sort_by=current_sort, limit=8)
        last_process_fetch = current_time

    processes = cached_processes

    if not processes:
        return layout

    if selected_index >= len(processes):
        selected_index = 0


    table = Table(expand=True, show_lines=True)
    table.add_column("PID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("CPU")
    table.add_column("MEM")

    for i, p in enumerate(processes):
        cpu_val = p["cpu_percent"]
        mem_val = p["memory_percent"]

        style = "reverse bold" if i == selected_index else ""

        table.add_row(
            str(p["pid"]),
            p["name"][:12],
            f"[{get_color(cpu_val)}]{get_bar(cpu_val)} {cpu_val:.1f}%[/]",
            f"[{get_color(mem_val)}]{get_bar(mem_val)} {mem_val:.1f}%[/]",
            style=style
        )

    layout["right"].update(
        Panel(
            table,
            title=f" Processes ({current_sort.upper()})",
            border_style="magenta"
        )
    )

    
    mood = get_system_mood(cpu)
    recommendation = get_kill_recommendation(processes)

    controls = Text()
    controls.append("Controls:\n", style="bold cyan")
    controls.append("⬆⬇ Navigate   ", style="yellow")
    controls.append("[C] CPU   ", style="green")
    controls.append("[M] Memory   ", style="yellow")
    controls.append("[K] Kill   ", style="red")
    controls.append("[Q] Quit\n", style="magenta")

    footer = Text()
    footer.append(f" System Mood: {mood}\n", style="bold")
    footer.append(f"\n Recommendation:\n{recommendation}\n\n")
    footer.append(controls)

    layout["footer"].update(
        Panel(footer, border_style="blue", title=" System Insights & Controls")
    )

    return layout



def handle_keys(processes):
    global current_sort, running, selected_index

    if msvcrt.kbhit():
        key = msvcrt.getch()

        if key == b'\xe0':
            key = msvcrt.getch()

            if key == b'H':
                selected_index = max(0, selected_index - 1)
            elif key == b'P':
                selected_index = min(len(processes) - 1, selected_index + 1)

        else:
            key = key.decode("utf-8").lower()

            if key == "c":
                current_sort = "cpu"
            elif key == "m":
                current_sort = "memory"
            elif key == "k":
                pid = processes[selected_index]["pid"]
                kill_process(pid)
            elif key == "q":
                running = False



def live_dashboard():
    global running

    with Live(generate_dashboard(), refresh_per_second=10) as live:
        while running:
            time.sleep(0.03)
            handle_keys(cached_processes)
            live.update(generate_dashboard())
