from fastapi import FastAPI
from app.api.routes.health import router as health_router



app = FastAPI(title="Workout Tracker API")



app.include_router(health_router)


@app.get("/")
def root():

    return {"message": "Workout Tracker API is running"}