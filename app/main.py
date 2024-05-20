from fastapi import FastAPI
from . import models
from .database import engine
from .routers import auth, posts, users, vote
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    'https://www.google.com',
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_mehods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get('/')
def home():
    return