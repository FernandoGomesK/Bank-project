from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from config.dependencies import get_db
from models.ClientModel import ClientModel
from schemas.ClientSchema import ClientCreate, ClientResponse

from utils.exceptions.client_exceptions import ClientAlreadyExistsException, ClientDoesntHaveCNPJException, ClientDoesntHaveCPFException

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
)

@router.post("/", response_model=ClientResponse)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    
    if client.client_type == "PF" and client.cpf:
        client_exists = db.query(ClientModel).filter(ClientModel.cpf == client.cpf).first()
        if client_exists:
            raise ClientAlreadyExistsException(client.client_id)
        
    if client.client_type == "PJ" and client.cnpj:
        client_exists = db.query(ClientModel).filter(ClientModel.cnpj == client.cnpj).first()
        if client_exists:
            raise ClientAlreadyExistsException(client.client_id)
          
    if client.clint_type == "PF" and not client.cpf:
        raise ClientDoesntHaveCPFException(client.client_id)
    
    if client.client_type == "PJ" and not client.cnpj:
        raise ClientDoesntHaveCNPJException(client.client_id)
    
    db_client = ClientModel(   
        name = client.name,
        client_type = client.client_type,
        cpf = client.cpf,
        birth_date = client.birth_date,
        cnpj = client.cnpj,
        company_name =  client.company_name,
        branch_id = client.branch_id
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.get("/", response_model=List[ClientResponse])
def read_clients(db: Session = Depends(get_db)):
    return db.query(ClientModel).all()
