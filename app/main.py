from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def health():
    return{
        "Message" : "Health Api is working Properly "
    }