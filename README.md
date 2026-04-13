Architecture Overview
---
 Frontend
* React (with Vite)
* Modern CSS / UI
---
 Backend
* REST APIs(fastAPI)
  
 Project Structure
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
```
System Monitor with Threat Detection

Overview
This project is an intelligent system monitoring dashboard that goes beyond traditional tools by combining **real-time performance tracking with threat detection and control**.

Unlike standard monitors, it not only shows system data but also **analyzes process behavior and enables immediate action**.

---

Key Features

 Intelligent Threat Detection
Analyzes running processes using CPU usage, memory consumption, and heuristic patterns to identify suspicious behavior.

 Real-Time Risk Scoring
Each process is assigned a dynamic risk level:
- 🟢 Safe  
- 🟡 Medium  
- 🔴 High  

 Threat-Aware Process Control
Detect → Evaluate → Act  
Users can instantly terminate high-risk processes directly from the dashboard.

 Live Alert System
Automatically notifies users when a high-risk process is detected.

 Interactive UI
Includes real-time graphs, CPU bars, filtering, and sorting for better visualization.

 Future Scope
- AI-based anomaly detection  
- Automated threat mitigation  
- Cross-platform support  

---

 WHERE IT STANDS OUT
A system that **monitors, detects, and responds** — not just displays data.

---
```

Getting Started

1. Clone the repo:
*git clone https://github.com/OMORJEEVAN/OS_HACKATHON.git
*cd OS_HACKATHON

2. Install requirements:
*pip install -r requirements.txt

4. Run Frontend:
*cd frontend
*npm install
*npm run dev

5. Run Backend:
*py -m uvicorn backend.app:app --reload

6. Run UI in terminal:
*cd cli
*run the main.py

Future Improvements:

* Backend API integration
* Authentication system
* Database integration
* Deployment (Vercel / Render)

Contribution:

This is a hackathon project, but suggestions and improvements are always welcome.

Author:
Arit Patra


Show your support:
If you like this project, give it a ⭐ on GitHub!
