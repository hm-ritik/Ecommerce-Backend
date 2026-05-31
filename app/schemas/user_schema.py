from pydantic import BaseModel , Field

class UserCreate(BaseModel):
    username:str
    name:str
    email:str
    phone_number:str
    password:str

class Login(BaseModel):
    email:str
    password:str

class UserResponse(BaseModel):
       id:int
       username:str
       name:str
       email:str
       phone_number:str
       user_role:str

