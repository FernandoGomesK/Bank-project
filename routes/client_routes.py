from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from config.dependencies import get_db
from models.ClientModel import ClientModel
from models.BranchModel import BranchModel
from schemas.ClientSchema import ClientCreate, ClientResponse

from utils.exceptions.client_exceptions import ClientAlreadyExistsException, ClientDoesntHaveCNPJException, ClientDoesntHaveCPFException, BranchDoesntExistException

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
)

@router.post("/", response_model=ClientResponse)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    
    if client.client_type == "PF" and client.cpf:
        client_exists = db.query(ClientModel).filter(ClientModel.cpf == client.cpf).first()
        if client_exists:
            raise ClientAlreadyExistsException(client.cpf)
        
    if client.client_type == "PJ" and client.cnpj:
        client_exists = db.query(ClientModel).filter(ClientModel.cnpj == client.cnpj).first()
        if client_exists:
            raise ClientAlreadyExistsException(client.cnpj)
          
    if client.client_type == "PF" and not client.cpf:
        raise ClientDoesntHaveCPFException("cadastro de pessoa física requer CPF.")
    
    if client.client_type == "PJ" and not client.cnpj:
        raise ClientDoesntHaveCNPJException("cadastro de pessoa jurídica requer CNPJ.")
    
    branch = db.query(BranchModel).filter(BranchModel.id == client.branch_id).first()
    if not branch:
        raise BranchDoesntExistException(client.branch_id)
    
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
