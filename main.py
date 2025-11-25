# main.py
from fastapi import FastAPI
from config.database import engine, Base
from routes import branch_routes

# 1. Cria as tabelas no banco de dados automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "O Banco Beto está ON! Acesse /docs para usar."}

# 2. Inclui as rotas do branch_routes
app.include_router(branch_routes.router)