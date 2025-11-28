from sqlalchemy import Column, Integer, String, ForeignKey
from config.database import Base

class ClientModel(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    client_type = Column(String(10))
    cpf = Column(String(11), unique=True, nullable=True)
    birth_date = Column(String(10), nullable=True)
    cnpj = Column(String(14), unique=True, nullable=True)
    company_name = Column(String(100), nullable=True)
    branch_id = Column(Integer, ForeignKey("branches.id"))
    password_hash = Column(String(255))      