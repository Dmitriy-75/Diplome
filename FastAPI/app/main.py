from fastapi import FastAPI, APIRouter
from app.routers import task
from app.routers import user
import uvicorn

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, log_level="info")


