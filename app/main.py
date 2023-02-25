from fastapi import FastAPI
from app.src.routers.user import router as UserRouter


# api descriptions
description = """
A Simple API to get/create/update/delete user data from a database
"""
app = FastAPI(title="Ryde Users", version="0.0.1", description=description)
app.include_router(UserRouter, tags=["User"], prefix="/api/users")


@app.get("/api/ping")
def root():
    return {"message": "Pong"}
