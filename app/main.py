from fastapi import FastAPI
from app.src.routers.user import router as UserRouter

app = FastAPI()
app.include_router(UserRouter, tags=["User"], prefix="/api/users")


@app.get("/api/ping")
def root():
    return {"message": "Pong"}
