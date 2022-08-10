
from pydantic import BaseModel, EmailStr

from database import Base

class auth (BaseModel):
   
    email : EmailStr
    password : str
    
class response(BaseModel):
    username : str
    email : EmailStr
    user_token:str
    
    class Config:
        orm_mode = True

class Create_User(BaseModel):
    username : str
    email : EmailStr
    password : str
    
    class Config:
        orm_mode = True
    
    
