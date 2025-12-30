from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from uuid import uuid4
import os

from api import ingest, query, chat, profile, auth
from services.db import Database

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Database.connect()
    yield
    await Database.disconnect()

app = FastAPI(
    title="Humanoid Robotics RAG API",
    version="0.1.0",
    lifespan=lifespan
)

# -----------------------
# CORS
# -----------------------
default_origins = [
    "http://localhost:3000",
    "http://localhost:3001",
]

allow_origins = default_origins + [
    "https://tabsheera-shakeel.github.io",
    "https://tabsheera-shakeel.github.io/Physical-AI-Humanoid-Robotics-Textbook",
    "https://physical-ai-humanoid-robotics-textbook.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# REQUIRED SESSION API ✅
# -----------------------
@app.post("/api/chat/sessions")
async def create_chat_session():
    return {"session_id": str(uuid4())}

# -----------------------
# Routers
# -----------------------
app.include_router(ingest.router, prefix="/api/v1", tags=["Ingestion"])
app.include_router(query.router, prefix="/api", tags=["Query"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])
app.include_router(auth.router, prefix="/api", tags=["Auth"])
app.include_router(profile.router, prefix="/api", tags=["Profile"])

# -----------------------
# Health
# -----------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}
