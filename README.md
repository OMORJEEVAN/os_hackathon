Architecture Overview

 Frontend
* React (with Vite)
* Modern CSS / UI

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
         └── schemas.py```
---

 Key Highlights

* Clean separation of frontend & backend
* Modular backend architecture (routers + services pattern)
* Scalable structure for future features

---

Getting Started

1. Clone the repo
git clone https://github.com/OMORJEEVAN/OS_HACKATHON.git
cd OS_HACKATHON

2. Run Frontend
cd frontend
npm install
npm run dev

3. Run Backend
py -m uvicorn backend.app:app --reload

4. Run UI in terminal
   cd cli
   run the main.py

Future Improvements

* Backend API integration
* Authentication system
* Database integration
* Deployment (Vercel / Render)

Contribution

This is a hackathon project, but suggestions and improvements are always welcome.

Author
Arit Patra


Show your support:
If you like this project, give it a ⭐ on GitHub!
