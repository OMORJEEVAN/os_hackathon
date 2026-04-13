import {
  ResponsiveContainer,
  AreaChart,
  Area,
  XAxis,
  Tooltip,
} from "recharts";
import { useState, useEffect } from "react";

export default function LineChartComp({ value }) {
  const [data, setData] = useState([]);

  useEffect(() => {
    setData((prev) => [
      ...prev.slice(-20),
      {
        time: new Date().toLocaleTimeString(),
        cpu: value,
      },
    ]);
  }, [value]);

  return (
    <div className="graph-card">

      {/* 🔥 BETTER TITLE */}
      <h2 className="graph-title">System Performance</h2>

      <ResponsiveContainer width="100%" height={280}>
        <AreaChart data={data}>
          
          <defs>
            <linearGradient id="colorCpu" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stopColor="#ff7a18" />
              <stop offset="100%" stopColor="#00f5d4" />
            </linearGradient>
          </defs>

          <XAxis
            dataKey="time"
            tick={{ fill: "#94a3b8", fontSize: 11 }}
            tickMargin={10}
            axisLine={false}
            tickLine={false}
          />

          <Tooltip
            contentStyle={{
              background: "#0f172a",
              border: "none",
              borderRadius: "10px",
              color: "white",
            }}
          />

          <Area
            type="monotone"
            dataKey="cpu"
            stroke="#ffffff"
            strokeWidth={2}
            fill="url(#colorCpu)"
            fillOpacity={0.3}
          />
        </AreaChart>
      </ResponsiveContainer>

    </div>
  );
}