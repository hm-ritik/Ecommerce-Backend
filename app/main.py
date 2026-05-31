from fastapi import FastAPI
from app.routes.user_routes import router as auth_router

app=FastAPI()
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"])


@app.get('/')
async def health():
    return{
        "Message" : "Health Api is working Properly "
    }