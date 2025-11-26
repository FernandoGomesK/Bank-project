# main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from config.database import engine, Base
from routes import client_routes

from utils.exceptions.BranchExceptions import BranchAlreadyExistsException
from utils.exceptions.error_handlers import branch_exists_handler

# 1. Cria as tabelas no banco de dados automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_exception_handler(BranchAlreadyExistsException, branch_exists_handler)



@app.get("/")
def read_root():
    return {"mensagem": "O Banco Beto está ON! Acesse /docs para usar."}

# 2. Inclui as rotas do branch_routes
app.include_router(client_routes.router)