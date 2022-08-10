
from fastapi import FastAPI, status, Depends,HTTPException
from database import get_db, engine
from sqlalchemy.orm import Session
import schemas
import models
from fastapi.middleware.cors import CORSMiddleware
from stream_chat import StreamChat

models.Base.metadata.create_all(bind=engine)

STREAM_KEY = "5ds3jqxc77yz"
STREAM_SECRET = "265tgj6hu6vpwyk7878aze6dntj5wdfytmgbx4t55ztdtbek79rx88dy82atvc9v"

app = FastAPI()

chat = StreamChat(api_key=STREAM_KEY, api_secret=STREAM_SECRET)

@app.post("/login",response_model=schemas.response)
def login_vol(user_credentials: schemas.auth , db: Session = Depends(get_db)):


    volunteer = db.query(models.User_details).filter(
         models.User_details.email == user_credentials.email,
                                models.User_details.password == user_credentials.password).first()
    
    if not volunteer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid user")
        
    return volunteer


# method to create a new user
@app.post("/register", response_model=schemas.response)
def register_vol(user_credentials: schemas.Create_User , db: Session = Depends(get_db)):
    stream_user = create_stream_user(id=user_credentials.username, name=user_credentials.username)
    user = models.User_details(user_token =stream_user ,username=user_credentials.username, email=user_credentials.email, password=user_credentials.password)
    db.add(user)
    db.commit()
   
    return user

# Method to create stream chat user

def create_stream_user(id:str, name:str):
    user = chat.upsert_user({"id": id, "name": name})
    return chat.create_token(user_id=id)


