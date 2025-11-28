from pydantic import BaseModel, field_validator
from utils.verifications.PhoneVerification import validate_phone_number


class BranchCreate(BaseModel):
    address: str
    phone: str

    @field_validator('phone')
    def phone_must_be_valid(cls, v):
        return validate_phone_number(v)

class BranchResponse(BaseModel):
    id: int
    address: str

    class Config:
        from_attributes = True

