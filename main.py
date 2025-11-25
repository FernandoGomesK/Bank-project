# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine, Base
from models.BranchModel import BranchModel
from schemas.BranchSchema import BranchCreate, BranchResponse

# 1. Cria as tabelas no banco de dados automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "O Banco Beto está ON! Acesse /docs para usar."}

# Função para pegar uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ROTA: Criar uma nova filial
# Em vez de chamar banco.add_branch(), o usuário faz um POST aqui
@app.post("/branches/", response_model=BranchResponse)
def create_branch(branch: BranchCreate, db: Session = Depends(get_db)):
    # 1. Cria o objeto do Modelo (Model) com os dados validados (Schema)
    db_branch = BranchModel(
        branch_id=branch.branch_id, 
        address=branch.address, 
        phone=branch.phone
    )
    
    # 2. Salva no MySQL
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    
    return db_branch

# ROTA: Listar filiais
@app.get("/branches/", response_model=list[BranchResponse])
def read_branches(db: Session = Depends(get_db)):
    # Faz um "SELECT * FROM filiais"
    return db.query(BranchModel).all()