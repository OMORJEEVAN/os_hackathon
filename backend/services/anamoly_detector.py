from backend.services.process_manager import get_all_processes


CPU_THRESHOLD = 50.0      # % CPU usage
MEMORY_THRESHOLD = 50.0  # % Memory usage


def detect_anomalies():
    """
    Detects processes exceeding CPU or memory thresholds
    """
    processes = get_all_processes()
    alerts = []

    for proc in processes:
        if proc["cpu_percent"] > CPU_THRESHOLD:
            alerts.append({
                "type": "HIGH_CPU",
                "pid": proc["pid"],
                "name": proc["name"],
                "value": proc["cpu_percent"],
                "message": f"High CPU usage: {proc['cpu_percent']}%"
            })

        if proc["memory_percent"] > MEMORY_THRESHOLD:
            alerts.append({
                "type": "HIGH_MEMORY",
                "pid": proc["pid"],
                "name": proc["name"],
                "value": proc["memory_percent"],
                "message": f"High Memory usage: {proc['memory_percent']:.2f}%"
            })

    return alerts