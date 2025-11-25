from sqlalchemy import Column, Integer, String, ForeignKey
from config.database import Base

class BranchModel(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    branch_id = Column(String(10), unique=True)
    address = Column(String(100))
    phone = Column(String(15))
