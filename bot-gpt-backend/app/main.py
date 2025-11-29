from fastapi import FastAPI
from app.database import Base, engine
from app.routers import conversations, messages

Base.metadata.create_all(bind=engine)

app = FastAPI(title="BOT GPT Backend")

app.include_router(conversations.router)
app.include_router(messages.router)
