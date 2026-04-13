import "../styles/card.css";

export default function StatsCard({ title, value }) {
  return (
    <div className="card glass">
      <h3>{title}</h3>
      <p>{value.toFixed(1)}%</p>
    </div>
  );
}