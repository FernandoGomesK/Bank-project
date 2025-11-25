from pydantic import BaseModel

class BranchCreate(BaseModel):
    branch__id: str
    adress: str
    phone: str

class BranchResponse(BaseModel):
    id: int
    Branch_id: str
    adress: str

    class Config:
        from_attributes = True

