from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from config.dependencies import get_db
from models.AccountModel import AccountModel
from models.ClientModel import ClientModel
from schemas.AccountSchema import AccountCreate

from utils.exceptions.Account_exceptions import ClientDoesntExistException, ClientAlreadyHasAccountException

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
)

@router.post("/")
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.client_id == account.client_id).first()
    
    if not client:
        raise ClientDoesntExistException(account.client_id)
    
    account_type_exists = db.query(AccountModel).filter(
        AccountModel.client_id == account.client_id,
        AccountModel.account_type == account.account_type
    ).first()
    
    if account_type_exists:
        raise ClientAlreadyHasAccountException(account.client_id, account.account_type)
    
    db_account = AccountModel(
        account_type=account.account_type,
        client_id=account.client_id,
        branch_id=client.branch_id,
        balance=0.0 
    )
    
    db.add(db_account)
    db.commit()
    db.refresh(db_account)

    return db_account