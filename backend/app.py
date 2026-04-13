from fastapi import FastAPI
from backend.routers import system_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(system_router.router)


# Root endpoint (just for testing)
@app.get("/")
def root():
    return {
        "message": "Smart Process Monitor API is running 🚀"
    }