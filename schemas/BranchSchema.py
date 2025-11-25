from pydantic import BaseModel

class BranchCreate(BaseModel):
    branch_id: str
    address: str
    phone: str

class BranchResponse(BaseModel):
    id: int
    branch_id: str
    address: str

    class Config:
        from_attributes = True

