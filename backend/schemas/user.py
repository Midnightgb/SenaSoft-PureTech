from pydantic import BaseModel, EmailStr
from enum import Enum
class Rol(Enum):
    Admin = 1
    Employee = 2
    vulnerable = 3
    non_vulnerable = 4

class UserBase(BaseModel):
    name: str
    email: EmailStr
    type: Rol
    eco_points: int = 0

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
