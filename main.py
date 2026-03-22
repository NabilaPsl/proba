from fastapi import FastAPI
from database import engine
from models import user_model
from routers.user_router import router as user_router

app = FastAPI()

user_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "API For superMarket is working"}

app.include_router(user_router)