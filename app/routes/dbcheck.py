from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from fastapi import APIRouter, Depends, HTTPException
from app.core.database import get_db

router=APIRouter()
@router.get("/test-db")
async def test_db(
    db: AsyncSession = Depends(get_db)
):
    await db.execute(text("SELECT 1"))
    return {"message": "DB connected"}
