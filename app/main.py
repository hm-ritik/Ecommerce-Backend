from fastapi import FastAPI
from app.routes import dbcheck 
app=FastAPI()
app.include_router(dbcheck.router)

@app.get('/')
async def health():
    return{
        "Message" : "Health Api is working Properly "
    }