from fastapi import APIRouter, Query

from backend.services.system_stat import get_system_stats
from backend.services.process_manager import (
    get_all_processes,
    get_top_processes,
    get_process_by_pid,
    kill_process
)
from backend.services.anamoly_detector import detect_anomalies

router = APIRouter()


# ------------------- RISK ENGINE -------------------

SUSPICIOUS_KEYWORDS = [
    "hack", "keylogger", "miner", "trojan", "malware", "inject", "stealer"
]


def calculate_risk(name, cpu, memory, path):
    risk = 0

    name = (name or "").lower()
    path = (path or "").lower()

    if any(k in name for k in SUSPICIOUS_KEYWORDS):
        risk += 50

    if cpu > 50:
        risk += 20
    elif cpu > 20:
        risk += 10

    if memory > 20:
        risk += 10

    if "temp" in path or "appdata" in path:
        risk += 20

    return risk


def get_risk_label(risk):
    if risk > 50:
        return "High"
    elif risk > 20:
        return "Medium"
    return "Safe"


def attach_risk(processes):
    updated = []

    for p in processes:
        risk_score = calculate_risk(
            p.get("name"),
            p.get("cpu_percent", 0),
            p.get("memory_percent", 0),
            p.get("exe", "")
        )

        p["risk"] = risk_score
        p["risk_label"] = get_risk_label(risk_score)

        updated.append(p)

    return updated


# ------------------- SYSTEM STATS -------------------

@router.get("/stats")
def stats():
    return get_system_stats()


# ------------------- PROCESSES -------------------

# 🔥 ALL PROCESSES (WITH RISK)
@router.get("/processes")
def processes():
    data = get_all_processes()
    return attach_risk(data)


# 🔥 SORTED PROCESSES
@router.get("/processes/sorted")
def sorted_processes(
    sort_by: str = Query("cpu", enum=["cpu", "memory", "risk"]),
    order: str = Query("desc", enum=["asc", "desc"])
):
    data = get_all_processes()
    data = attach_risk(data)

    reverse = True if order == "desc" else False

    key_map = {
        "cpu": "cpu_percent",
        "memory": "memory_percent",
        "risk": "risk"
    }

    return sorted(data, key=lambda x: x.get(key_map[sort_by], 0), reverse=reverse)


# 🔥 TOP PROCESSES (WITH RISK)
@router.get("/processes/top")
def top_processes(sort_by: str = "cpu", limit: int = 5):
    data = get_top_processes(sort_by, limit)
    return attach_risk(data)


# 🔥 FILTER BY RISK LEVEL
@router.get("/processes/risk/{level}")
def processes_by_risk(level: str):
    data = get_all_processes()
    data = attach_risk(data)

    level = level.capitalize()

    return [p for p in data if p["risk_label"] == level]


# 🔥 SINGLE PROCESS DETAIL
@router.get("/process/{pid}")
def process_detail(pid: int):
    p = get_process_by_pid(pid)
    if not p:
        return {}

    enriched = attach_risk([p])
    return enriched[0]


# ------------------- PROCESS CONTROL -------------------

# 🔥 KILL PROCESS
@router.post("/process/kill/{pid}")
def kill(pid: int):
    return kill_process(pid)


# 🔥 BULK KILL (VERY COOL FEATURE 🔥)
@router.post("/process/kill/bulk")
def kill_bulk(pids: list[int]):
    results = []

    for pid in pids:
        results.append({
            "pid": pid,
            "result": kill_process(pid)
        })

    return results


# ------------------- ALERTS -------------------

# 🔥 ANOMALY DETECTION
@router.get("/alerts")
def alerts():
    return detect_anomalies()


# 🔥 HIGH RISK ALERTS ONLY
@router.get("/alerts/high-risk")
def high_risk_alerts():
    data = get_all_processes()
    data = attach_risk(data)

    return [p for p in data if p["risk"] > 50]