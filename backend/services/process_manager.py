import psutil

def get_all_processes():
    """
    Returns a list of all running processes with updated CPU usage
    """
    processes = []

    
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(None)
        except:
            continue

    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info

            
            if not info['name'] or info['name'] == "System Idle Process":
                continue

            processes.append({
                "pid": info['pid'],
                "name": info['name'],
                "cpu_percent": info['cpu_percent'],
                "memory_percent": info['memory_percent']
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return processes


def get_top_processes(sort_by="cpu", limit=5):
    """
    Returns top processes sorted by CPU or memory usage
    """
    processes = get_all_processes()

    key = "cpu_percent" if sort_by == "cpu" else "memory_percent"

    sorted_processes = sorted(
        processes,
        key=lambda x: x[key],
        reverse=True
    )

    return sorted_processes[:limit]


def get_process_by_pid(pid):
    """
    Returns detailed info about a specific process
    """
    try:
        proc = psutil.Process(pid)

        return {
            "pid": proc.pid,
            "name": proc.name(),
            "status": proc.status(),
            "cpu_percent": proc.cpu_percent(interval=0.5),
            "memory_percent": proc.memory_percent(),
            "threads": proc.num_threads()
        }

    except psutil.NoSuchProcess:
        return {"error": "Process not found"}

    except psutil.AccessDenied:
        return {"error": "Access denied"}


def kill_process(pid):
    """
    Safely kills a process by PID
    """
    try:
        proc = psutil.Process(pid)
        proc.terminate()  

        return {
            "status": "success",
            "message": f"Process {pid} terminated"
        }

    except psutil.NoSuchProcess:
        return {"status": "error", "message": "Process not found"}

    except psutil.AccessDenied:
        return {"status": "error", "message": "Access denied"}
