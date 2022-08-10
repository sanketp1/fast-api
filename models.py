from enum import unique
from multiprocessing import Value
from pickle import TRUE
from unicodedata import name
from sqlalchemy.dialects.postgresql import UUID
from database import Base
from sqlalchemy import Column,Integer,String,TIMESTAMP,Boolean,ForeignKey
from sqlalchemy.sql.expression import text
import sqlalchemy.dialects.postgresql as postgresql
from sqlalchemy.dialects.postgresql import UUID

class User_details(Base):
    __tablename__ = "user_details"
    
    username = Column(String, nullable=False, unique=True)
    email = Column (String, nullable= False, unique= True, primary_key = True)
    password = Column (String, nullable= False)
    user_token = Column(String,nullable=True)