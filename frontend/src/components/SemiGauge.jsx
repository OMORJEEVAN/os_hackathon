import "../styles/SemiGauge.css";

export default function SemiGauge({ value }) {
  const circumference = 283; 
  const offset = circumference - (circumference * value) / 100;

  return (
    <div className="semi-wrapper glass">
      <div className="semi-container">

        <svg className="semi-svg" viewBox="0 0 200 120">

         
          <defs>
            <linearGradient id="gradient">
              <stop offset="0%" stopColor="#00f5d4" />
              <stop offset="100%" stopColor="#00bbf9" />
            </linearGradient>
          </defs>

        
          <path
            d="M10 110 A90 90 0 0 1 190 110"
            className="semi-bg"
          />

          
          <path
            d="M10 110 A90 90 0 0 1 190 110"
            className="semi-progress"
            stroke="url(#gradient)"   
            style={{
              strokeDasharray: circumference,
              strokeDashoffset: offset,
            }}
          />

        </svg>

       
        <div className="semi-center">
          <h2>{value.toFixed(0)}</h2>
          <span>%</span>
          <p>CPU Usage</p>
        </div>

      </div>
    </div>
  );
}
