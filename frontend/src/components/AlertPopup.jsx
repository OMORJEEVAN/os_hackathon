import "../styles/alert.css";

export default function AlertPopup({ alerts }) {
  if (!alerts.length) return null;

  return (
    <div className="alert-container">
      {alerts.map((p) => (
        <div key={p.pid} className="alert-box">
          🚨 High Risk Process Detected: <b>{p.name}</b>
        </div>
      ))}
    </div>
  );
}