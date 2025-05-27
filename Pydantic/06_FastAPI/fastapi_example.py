from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class Settings(BaseModel):
    app_name: str = "Pikachu app"
    admin_email: EmailStr = "pikachu@pokemon.com"
    
def get_settings():
    return Settings()

@app.post("/signup")
def signup(user: UserSignup):
    return {"message": f"Hello {user.username}"}

@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings