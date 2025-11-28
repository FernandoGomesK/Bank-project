from pydantic import BaseModel, field_validator
from typing import Optional
from utils.verifications.PhoneVerification import validate_phone_number

class ClientCreate(BaseModel):
    name: str
    branch_id: int
    client_type: str
    phone: str
    
    cpf: Optional[str] = None
    birth_date: Optional[str] = None
    cnpj: Optional[str] = None
    company_name: Optional[str] = None
    password: str
    
    @field_validator('phone')
    def phone_must_be_valid(cls, v):
        
        return validate_phone_number(v)
class ClientResponse(BaseModel):
    client_id: int
    name: str
    branch_id: int
    client_type: str
    phone: str
    
    cpf: Optional[str] = None
    birth_date: Optional[str] = None
    cnpj: Optional[str] = None
    company_name: Optional[str] = None

    class Config:
        from_attributes = True