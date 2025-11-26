from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from config.dependencies import get_db
from models.BranchModel import BranchModel
from schemas.BranchSchema import BranchCreate, BranchResponse

from utils.exceptions.BranchExceptions import BranchAlreadyExistsException

router = APIRouter(
    prefix="/branches",
    tags=["branches"],
)

@router.post("/", response_model=BranchResponse)
def create_branch(branch: BranchCreate, db: Session = Depends(get_db)):
    branch_exists = db.query(BranchModel).filter(BranchModel.branch_id == branch.branch_id).first()
    if branch_exists:
        raise BranchAlreadyExistsException(branch.branch_id)
    
    db_branch = BranchModel(
        address=branch.address, 
        phone=branch.phone
    )
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch

@router.get("/", response_model=List[BranchResponse])
def read_branches(db: Session = Depends(get_db)):
    return db.query(BranchModel).all()
