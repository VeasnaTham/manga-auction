from pydantic import BaseModel
import datetime

class UserModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class Detail(BaseModel):
    email: str
    password: str

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class TokenCreate(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str
    status: bool
    create_date: datetime.datetime

class ChangePassword(BaseModel):
    email: str
    old_password: str
    new_password: str