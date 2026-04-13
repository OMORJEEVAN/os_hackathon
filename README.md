# System Monitor with Threat Detection

## Overview
This project is an intelligent system monitoring dashboard that goes beyond traditional tools by combining real-time performance tracking with threat detection and control.

Unlike standard system monitors, it not only displays system data but also analyzes process behavior and enables immediate action.

---

## Architecture Overview

### Frontend
- React (with Vite)
- Modern CSS and UI components

### Backend
- REST APIs using FastAPI

---

## Project Structure
```
OS_HACKATHON/
├── test.py
├── frontend/
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── vite.config.js
│   ├── src/
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   ├── main.jsx
│   │   ├── styles/
│   │   │   ├── alert.css
│   │   │   ├── card.css
│   │   │   ├── circleDial.css
│   │   │   ├── dashboard.css
│   │   │   ├── semiGauge.css
│   │   │   └── table.css
│   │   ├── services/
│   │   │   └── api.js
│   │   └── components/
│   │       ├── AlertPopup.jsx
│   │       ├── CircleDial.jsx
│   │       ├── CpuGauge.jsx
│   │       ├── Dashboard.jsx
│   │       ├── LineChart.jsx
│   │       ├── ProcessTable.jsx
│   │       ├── SemiGauge.jsx
│   │       └── StatsCard.jsx
│   ├── 
├── cli/
│   ├── commands.py
│   ├── main.py
│   ├── ui.py
│   
└── backend/
    ├── app.py
    ├── __init__.py 
    ├── utils/
    └── helper.py
     ├── services/
     │   ├── anamoly_detector.py
     │   ├── process_manager.py
     │   ├── system_stat.py
     │   ├── __init__.py
     │   
     ├── routers/
     │   ├── system_router.py
     │   ├── __init__.py
     │   
     │ 
     └── models/
         └── schemas.py
```

---

## Key Features

### Intelligent Threat Detection
Analyzes running processes using CPU usage, memory consumption, and heuristic patterns to identify suspicious behavior.

### Real-Time Risk Scoring
Each process is assigned a dynamic risk level:
- Safe  
- Medium  
- High  

### Threat-Aware Process Control
Implements a workflow of detection, evaluation, and action.  
Users can terminate high-risk processes directly from the dashboard.

### Live Alert System
Automatically notifies users when a high-risk process is detected.

### Interactive UI
Provides real-time graphs, CPU usage visualization, filtering, and sorting for better clarity and control.

---

## Key Insight

This system transforms passive monitoring into active decision-making.  
It enables users not only to observe system behavior but also to detect and respond to potential threats in real time.

---

## Getting Started

### 1. Clone the Repository
git clone https://github.com/OMORJEEVAN/OS_HACKATHON.git

cd OS_HACKATHON

### 2. Install Backend Requirements
pip install -r requirements.txt

### 3. Run Backend
py -m uvicorn backend.app:app --reload

### 4. Run Frontend
cd frontend
npm install
npm run dev

### 5. Access the Application
http://localhost:5173/

### 6. Run CLI Interface
cd cli
python main.py



---

## Future Improvements

- AI-based anomaly detection  
- Automated threat mitigation  
- Authentication system  
- Database integration  
- Deployment (Vercel / Render)  

---

## Contribution

This project was developed as part of a hackathon.  
Contributions, suggestions, and improvements are welcome.

---

## Author

Arit Patra

---

## Support

If you find this project useful, consider giving it a star on GitHub.
