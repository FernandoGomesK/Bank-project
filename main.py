# main.py
from fastapi import FastAPI
from config.database import engine, Base


from routes import client_routes, branch_routes, account_rotes, auth_routes


from utils.exceptions.BranchExceptions import BranchAlreadyExistsException
from utils.exceptions.error_handlers import branch_exists_handler
from utils.exceptions.client_exceptions import (ClientAlreadyExistsException, ClientDoesntHaveCNPJException,
                                                ClientDoesntHaveCPFException, BranchDoesntExistException)
from utils.exceptions.error_handlers import (client_exists_handler, client_missing_cnpj_handler, 
                                             client_missing_cpf_handler, branch_doesnt_exist_handler)
from utils.exceptions.auth_exceptions.InvalidCredentialsException import InvalidCredentialsException
from utils.exceptions.error_handlers import invalid_credentials_handler

# 1. Cria as tabelas no banco de dados automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_exception_handler(BranchAlreadyExistsException, branch_exists_handler)
app.add_exception_handler(ClientAlreadyExistsException, client_exists_handler)
app.add_exception_handler(ClientDoesntHaveCNPJException, client_missing_cnpj_handler)
app.add_exception_handler(ClientDoesntHaveCPFException, client_missing_cpf_handler)
app.add_exception_handler(BranchDoesntExistException, branch_doesnt_exist_handler)
app.add_exception_handler(InvalidCredentialsException, invalid_credentials_handler)

@app.get("/")
def read_root():
    return {"mensagem": "O Banco Beto está ON! Acesse /docs para usar."}

# 2. Inclui as rotas do branch_routes
app.include_router(branch_routes.router)
app.include_router(client_routes.router)
app.include_router(account_rotes.router)
app.include_router(auth_routes.router)