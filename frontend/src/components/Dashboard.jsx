import { useEffect, useState } from "react";
import { fetchStats, fetchProcesses } from "../services/api";

import CircleDial from "./CircleDial";
import LineChartComp from "./LineChart";
import ProcessTable from "./ProcessTable";

import "../styles/dashboard.css";

export default function Dashboard() {
  const [stats, setStats] = useState(null);
  const [processes, setProcesses] = useState([]);

  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const statsRes = await fetchStats();
        const procRes = await fetchProcesses();

        setStats(statsRes.data);
        setProcesses(procRes.data);
      } catch (err) {
        console.error(err);
      }
    }, 1500); 

    return () => clearInterval(interval);
  }, []);

  if (!stats) return <div className="loading">Loading...</div>;

  return (
    <div className="dashboard">

      
      <div className="top-row">
        <CircleDial value={stats.cpu.total_cpu_percent} label="CPU" />
        <CircleDial value={stats.memory.percent} label="Memory" />
        <CircleDial value={stats.disk.percent} label="Disk" />
      </div>

     
      <div className="graph-full glass">
        <LineChartComp value={stats.cpu.total_cpu_percent} />
      </div>

    
      <ProcessTable processes={processes} />
    </div>
  );
}
