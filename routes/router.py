
from fastapi import FastAPI
from fastapi import APIRouter
from models.models_ import UserCreate
import repository.user_respository as repo

router =APIRouter =(prefix ='/users' ,tags=['users'])
@router.post('/')

def create_user(user:UserCreate):
    res = repo.create_user(user.name,user.email)
    return {
        "id": res[0],
        "name" :res[1],
        "email":res[3]
    }



