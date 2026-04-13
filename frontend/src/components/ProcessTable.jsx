import { useState, useEffect } from "react";
import { killProcess } from "../services/api";
import AlertPopup from "./AlertPopup";
import "../styles/table.css";

export default function ProcessTable({ processes }) {
  const [selected, setSelected] = useState(null);
  const [alerts, setAlerts] = useState([]);

  const [sortBy, setSortBy] = useState("cpu");
  const [filter, setFilter] = useState("All");
  const [visibleCount, setVisibleCount] = useState(6);

 
  useEffect(() => {
    if (!processes.length) return;

    const highRisk = processes.filter((p) => p.risk > 50);
    setAlerts(highRisk.slice(0, 2));

    const timer = setTimeout(() => setAlerts([]), 4000);

    return () => clearTimeout(timer);
  }, [processes]);

 
  const filteredData = processes
    .filter((p) => {
      if (filter === "All") return true;
      return (p.risk_label || "Safe") === filter;
    })
    .sort((a, b) => {
      const keyMap = {
        cpu: "cpu_percent",
        memory: "memory_percent",
        risk: "risk",
      };
      return (b[keyMap[sortBy]] || 0) - (a[keyMap[sortBy]] || 0);
    });

  
  const handleKill = async (pid) => {
    try {
      console.log("Killing:", pid);
      await killProcess(pid);
      alert(` Process ${pid} killed`);
    } catch (err) {
      console.error(err);
      alert(" Kill failed");
    }
  };

  return (
    <div className="glass table-container">
      <AlertPopup alerts={alerts} />

      <h2 className="table-title">Threat Monitor</h2>

     
      <div className="controls">
        <div className="filters">
          {["All", "Safe", "Medium", "High"].map((f) => (
            <button
              key={f}
              className={filter === f ? "active" : ""}
              onClick={() => setFilter(f)}
            >
              {f}
            </button>
          ))}
        </div>

        <div className="custom-select">
          <select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
          >
            <option value="cpu">Sort by CPU</option>
            <option value="memory">Sort by Memory</option>
            <option value="risk">Sort by Risk</option>
          </select>
        </div>
      </div>

     
      <table className="table">
        <thead>
          <tr>
            <th>PID</th>
            <th>Process</th>
            <th>CPU</th>
            <th>Memory</th>
            <th>Threat</th>
            <th></th>
          </tr>
        </thead>

        <tbody>
          {filteredData.slice(0, visibleCount).map((p, index) => (
            <tr
              key={p.pid}
              className={`row 
                ${selected === p.pid ? "active" : ""} 
                ${p.risk > 50 ? "danger" : ""}
                ${index === 0 ? "top-process" : ""}
              `}
              onClick={() => setSelected(p.pid)}
            >
              <td>{p.pid}</td>

              <td className="process-cell">
                <span className="icon">{getIcon(p.name)}</span>
                {p.name}
              </td>

              <td>
                <div className="cpu-bar">
                  <div
                    className="cpu-fill"
                    style={{ width: `${p.cpu_percent || 0}%` }}
                  />
                </div>
                {(p.cpu_percent || 0).toFixed(1)}%
              </td>

              <td>{(p.memory_percent || 0).toFixed(1)}%</td>

              <td>
                <span className={`chip ${(p.risk_label || "safe").toLowerCase()}`}>
                  {p.risk_label || "Safe"}
                </span>
              </td>

              <td>
                {selected === p.pid && (
                  <button
                    className="kill-btn"
                    onClick={(e) => {
                      e.stopPropagation();
                      handleKill(p.pid);
                    }}
                  >
                    Kill
                  </button>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

     
      <div className="show-more-container">
        {visibleCount < filteredData.length ? (
          <button
            className="show-more-btn"
            onClick={() => setVisibleCount((prev) => prev + 6)}
          >
            Show More
          </button>
        ) : (
          <button
            className="show-more-btn"
            onClick={() => setVisibleCount(6)}
          >
            Show Less
          </button>
        )}
      </div>
    </div>
  );
}


function getIcon(name = "") {
  name = name.toLowerCase();

  if (name.includes("chrome") || name.includes("brave")) return "🌐";
  if (name.includes("python")) return "🐍";
  if (name.includes("system")) return "⚙️";
  if (name.includes("audio")) return "🔊";

  return "🧩";
}
