from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.users import router as users_router


# Create FastAPI app instance
app = FastAPI(title="Workout Tracker API")


# Include health routes
app.include_router(health_router)

# Include user routes
app.include_router(users_router)


# Root route to check if API is running
@app.get("/")
def root():
    return {"message": "Workout Tracker API is running"}