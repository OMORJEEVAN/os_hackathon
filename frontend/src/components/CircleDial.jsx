import "../styles/circleDial.css";

export default function CircleDial({ value, label }) {
  const angle = (value / 100) * 360;

  return (
    <div className="circle-wrapper glass">
      <div
        className="circle-ring"
        style={{
          background: `conic-gradient(
            #00f5d4 ${angle}deg,
            rgba(255,255,255,0.08) ${angle}deg
          )`,
        }}
      >
        <div className="circle-inner">
          <h2>{value.toFixed(0)}%</h2>
          <p>{label}</p>
        </div>
      </div>
    </div>
  );
}