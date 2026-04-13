import psutil


def get_cpu_stats():
    """
    Returns CPU usage (total + per core)
    """

    per_core = psutil.cpu_percent(interval=None, percpu=True)
    total = sum(per_core) / len(per_core)

    return {
        "total_cpu_percent": total,
        "per_core_percent": per_core
    }


def get_memory_stats():
    """
    Returns memory usage details
    """
    mem = psutil.virtual_memory()

    return {
        "total": mem.total,
        "available": mem.available,
        "used": mem.used,
        "percent": mem.percent
    }


def get_disk_stats():
    """
    Returns disk usage details
    """
    disk = psutil.disk_usage('/')

    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent": disk.percent
    }


def get_system_stats():
    """
    Combined system stats (for /stats endpoint)
    """
    return {
        "cpu": get_cpu_stats(),
        "memory": get_memory_stats(),
        "disk": get_disk_stats()
    }