from pydantic import BaseModel
from typing import Optional

class ClientCreate(BaseModel):
    name: str
    branch_id: int
    client_type: str
    
    cpf: Optional[str] = None
    birth_date: Optional[str] = None
    cnpj: Optional[str] = None
    company_name: Optional[str] = None
    
class ClientResponse(BaseModel):
    client_id: int
    name: str
    branch_id: int
    client_type: str
    
    cpf: Optional[str] = None
    birth_date: Optional[str] = None
    cnpj: Optional[str] = None
    company_name: Optional[str] = None

    class Config:
        from_attributes = True