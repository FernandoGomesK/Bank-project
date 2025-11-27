from sqlalchemy import Column, Integer, Float, String, ForeignKey
from config.database import Base

class AccountModel(Base):
    __tablename__ = "accounts"

    account_id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.client_id"))
    branch_id = Column(Integer, ForeignKey("branches.id"))
    balance = Column(Float, default=0.0)
    account_type = Column(String(20))