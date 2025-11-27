from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from config.dependencies import get_db
from utils.exceptions.auth_exceptions.InvalidCredentialsException import InvalidCredentialsException
from models.ClientModel import ClientModel
from utils.security import verify_password

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

class LoginRequest(BaseModel):
    identifier: str  # CPF or CNPJ
    password: str
    
@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(
        (ClientModel.cpf == request.identifier) | (ClientModel.cnpj == request.identifier)
    ).first()
    
    if not client or not verify_password(request.password, client.hashed_password):
        raise InvalidCredentialsException()
    
    return {"message": "Login successful", "client_id": client.client_id}