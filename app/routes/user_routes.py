from fastapi import APIRouter , Depends 
from sqlalchemy.ext.asyncio import AsyncSession 
from app.core.database import  get_db
from app.services.auth_services import register_user,login_user
from app.schemas.user_schema import UserCreate , Login , UserResponse

router=APIRouter()

@router.post("/register",response_model=UserResponse)
async def create_a_user(post:UserCreate , db:AsyncSession=Depends(get_db)):
    return await  register_user(db , post)

@router.post("/login")
async def making_login(post:Login , db:AsyncSession=Depends(get_db)):
    return await login_user(db , post)

