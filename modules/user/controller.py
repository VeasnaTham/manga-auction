from functools import wraps
from fastapi import APIRouter, Depends, HTTPException, status
from pymongo import MongoClient
from modules.user.dependency import get_db
from modules.user import model
from modules.user.utils import get_hashed_password, verify_password, create_access_token, create_refresh_token
from modules.user.auth_bearer import JWTBearer
from jose import jwt
import datetime
from core.database import user_collection


router = APIRouter(
    prefix="/user",
    tags=["Üser"]
)
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = "narscbjim@$@&^@&%^&RFghgjvbdsha" 
JWT_REFRESH_SECRET_KEY = "13ugfdfgh@#$%^@&jkl45678902"

@router.post("/register")
def register_user(user: model.UserModel, session: MongoClient = Depends(get_db)):
    try:
        existing_user = session.query(model.UserModel).filter_by(email=user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        encrypted_password =get_hashed_password(user.password)

        new_user = model.UserModel(username=user.username, email=user.email, password=encrypted_password )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return {"message":"user created successfully"}
    except Exception as e:
        print("Error", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post('/login' ,response_model=model.TokenSchema)
def login(request: model.Detail, db: MongoClient = Depends(get_db)):
    user = db.query(model.UserModel).filter(model.UserModel.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email")
    hashed_pass = user.password
    if not verify_password(request.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    
    access=create_access_token(user.id)
    refresh = create_refresh_token(user.id)

    token_db = model.TokenCreate(user_id=user.id,  access_toke=access,  refresh_toke=refresh, status=True)
    db.add(token_db)
    db.commit()
    db.refresh(token_db)
    return {
        "access_token": access,
        "refresh_token": refresh,
    }

@router.get('/getusers')
def getusers( dependencies=Depends(JWTBearer()),session: MongoClient = Depends(get_db)):
    user = session.query(model.UserModel).all()
    return user

@router.post('/change-password')
def change_password(request: model.ChangePassword, db: MongoClient = Depends(get_db)):
    user = db.query(model.UserModel).filter(model.UserModel.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    
    if not verify_password(request.old_password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid old password")
    
    encrypted_password = get_hashed_password(request.new_password)
    user.password = encrypted_password
    db.commit()
    
    return {"message": "Password changed successfully"}

@router.post('/logout')
def logout(dependencies=Depends(JWTBearer()), db: MongoClient = Depends(get_db)):
    token=dependencies
    payload = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
    user_id = payload['sub']
    token_record = db.query(model.TokenCreate).all()
    info=[]
    for record in token_record :
        print("record",record)
        if (datetime.utcnow() - record.created_date).days >1:
            info.append(record.user_id)
    if info:
        existing_token = db.query(model.TokenCreate).where(model.TokenCreate.user_id.in_(info)).delete()
        db.commit()
        
    existing_token = db.query(model.TokenCreate).filter(model.TokenCreate.user_id == user_id, model.TokenCreate.access_token==token).first()
    if existing_token:
        existing_token.status=False
        db.add(existing_token)
        db.commit()
        db.refresh(existing_token)
    return {"message":"Logout Successfully"} 

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
    
        payload = jwt.decode(kwargs['dependencies'], JWT_SECRET_KEY, ALGORITHM)
        user_id = payload['sub']
        data= kwargs['session'].query(model.TokenCreate).filter_by(user_id=user_id,access_toke=kwargs['dependencies'],status=True).first()
        if data:
            return func(kwargs['dependencies'],kwargs['session'])
        
        else:
            return {'msg': "Token blocked"}
        
    return wrapper