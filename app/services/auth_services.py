from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user_schema import UserCreate , Login
from app.repositories.user_repo import create_user , get_user_by_email , get_user_by_username
from app.core.security import hash_password , verify_password


async def register_user(db:AsyncSession , user_data:UserCreate):
    existing_email=await get_user_by_email(db ,user_data.email)
    if existing_email:
        raise ValueError("Email Already Exists")
    
    existing_username=await get_user_by_username(db,user_data.username)
    if existing_username:
        raise ValueError("Username Already Exists")
    
    user= User(
        username=user_data.username,
        email=user_data.email,
        phone_number=user_data.phone_number,
        name=user_data.name,
        password_hash=hash_password(
            user_data.password
        )
    )
    return await create_user(db , user)

async def login_user(db:AsyncSession , login_data:Login):
    existing_user=await get_user_by_email(db ,login_data.email )
    if not existing_user:
        raise ValueError("Create Account User Does not exists")
    if not verify_password(
        login_data.password,
        existing_user.password_hash
    ):
        raise ValueError("Email or Password is InValid")
    return existing_user


        
    
   
        


