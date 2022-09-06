from fastapi import FastAPI
 
from server.database import init_db
from server.routes.noticias import router as NoticiasRouter
 
 
app = FastAPI()
app.include_router(NoticiasRouter, tags=["noticias"], prefix="/noticias")

 
@app.on_event("startup")
async def start_db():
    await init_db()
 
 
@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}
    