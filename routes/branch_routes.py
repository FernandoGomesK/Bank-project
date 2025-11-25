from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from config.dependencies import get_db
from models.BranchModel import BranchModel
from schemas.BranchSchema import BranchCreate, BranchResponse

router = APIRouter(
    prefix="/branches",
    tags=["branches"],
)

@router.post("/", response_model=BranchResponse)
def create_branch(branch: BranchCreate, db: Session = Depends(get_db)):
    db_branch = BranchModel(
        branch_id=branch.branch_id, 
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
