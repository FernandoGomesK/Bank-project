from pydantic import BaseModel

class BranchCreate(BaseModel):
    address: str
    phone: str

class BranchResponse(BaseModel):
    id: int
    address: str

    class Config:
        from_attributes = True

