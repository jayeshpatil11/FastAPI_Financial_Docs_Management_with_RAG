from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.security import OAuth2PasswordRequestForm

from ..models import User
from ..auth import hash_password, verify_password, create_token
from ..deps import get_db

router = APIRouter(prefix="/auth")


# REGISTER
@router.post("/register")
#def register(username: str, password: str, db: Session = Depends(get_db)):
def register(username: str, password: str, role: str = "Client", db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    try:
        user = User(username=username, password=hash_password(password),role=role)
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"msg": "Registered successfully"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({
        "user_id": user.id,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }





'''
#  LOGIN (IMPORTANT FIX)
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({
        "user_id": user.id,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
'''

"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..models import User
#from ..auth import hash_password
from ..auth import hash_password, verify_password, create_token
from ..deps import get_db



router = APIRouter(prefix="/auth")

@router.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    # check existing
    existing = db.query(User).filter(User.username == username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    try:
        user = User(username=username, password=hash_password(password))
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"msg": "Registered successfully"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))







'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import User
from ..auth import hash_password, verify_password, create_token
from ..deps import get_db

router = APIRouter(prefix="/auth")
'''
'''
@router.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    user = User(username=username, password=hash_password(password))
    db.add(user)
    db.commit()
    return {"msg": "Registered"}
'''
'''
@router.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == username).first()

    if existing_user:
        return {"error": "Username already exists"}

    user = User(username=username, password=hash_password(password))
    db.add(user)
    db.commit()

    return {"msg": "Registered successfully"}

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return {"error": "User not found"}

    if not verify_password(password, user.password):
        return {"error": "Wrong password"}

    token = create_token({"user_id": user.id, "role": user.role})
    return {"token": token}
'''
@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.password):
        return {"error": "Invalid credentials"}

    token = create_token({"user_id": user.id, "role": user.role})
    return {"token": token}
"""