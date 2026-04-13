import "../styles/card.css";

export default function CpuGauge({ value }) {
  const angle = (value / 100) * 180;

  return (
    <div className="gauge">
      <div className="gauge-body">
        <div
          className="gauge-fill"
          style={{ transform: `rotate(${angle}deg)` }}
        ></div>
        <div className="gauge-cover">{value.toFixed(0)}%</div>
      </div>
      <p>CPU Usage</p>
    </div>
  );
}