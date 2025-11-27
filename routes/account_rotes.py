from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from config.dependencies import get_db

from models.AccountModel import AccountModel
from schemas.AccountSchema import AccountCreate, AccountResponse

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
)

@router.post("/")
def create_account(db: Session = Depends(get_db)):
    pass