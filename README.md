Architecture Overview

 Frontend
* React (with Vite)
* Modern CSS / UI

 Backend
* REST APIs(fastAPI)
  
 Project Structure
```
OS_HACKATHON/
│
├── frontend/                 # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/                  # Python backend
   ├── app.py                # Entry point
   │
   ├── models/               # Data models & schemas
   │   └── schemas.py
   │
   ├── routers/              # API routes
   │   ├── __init__.py
   │   └── system_router.py
   │
   ├── services/             # logic
   │   ├── anomaly_detector.py
   │   ├── process_manager.py
   │   └── system_stat.py
   │
   ├── utils/                # Helper functions
   │   └── helper.py
   │
   ├── data/                 # Data storage
   ├── cli/                  # CLI tools
   └── __pycache__/          # Ignored files
```

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
