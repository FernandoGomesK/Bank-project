from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# Importe TODAS as suas exceções aqui
from utils.exceptions.BranchExceptions import BranchAlreadyExistsException
from utils.exceptions.client_exceptions import (
    ClientAlreadyExistsException, ClientDoesntHaveCNPJException,
    ClientDoesntHaveCPFException, BranchDoesntExistException
)
from utils.exceptions.auth_exceptions.InvalidCredentialsException import InvalidCredentialsException
from utils.exceptions.Account_exceptions import ClientDoesntExistException, ClientAlreadyHasAccountException
from utils.exceptions.general_exceptions import InvalidNumberException

# Importe TODOS os seus handlers aqui
from utils.exceptions.error_handlers import (
    branch_exists_handler, client_exists_handler, client_missing_cnpj_handler,
    client_missing_cpf_handler, branch_doesnt_exist_handler, invalid_credentials_handler,
    client_doesnt_exist_handler, client_already_has_account_handler, invalid_number_handler
)

def register_exception_handlers(app: FastAPI):
    """Registra todas as exceções do sistema no app FastAPI."""
    
    app.add_exception_handler(BranchAlreadyExistsException, branch_exists_handler)
    app.add_exception_handler(ClientAlreadyExistsException, client_exists_handler)
    app.add_exception_handler(ClientDoesntHaveCNPJException, client_missing_cnpj_handler)
    app.add_exception_handler(ClientDoesntHaveCPFException, client_missing_cpf_handler)
    app.add_exception_handler(BranchDoesntExistException, branch_doesnt_exist_handler)
    app.add_exception_handler(InvalidCredentialsException, invalid_credentials_handler)
    app.add_exception_handler(ClientDoesntExistException, client_doesnt_exist_handler)
    app.add_exception_handler(ClientAlreadyHasAccountException, client_already_has_account_handler)
    app.add_exception_handler(InvalidNumberException, invalid_number_handler)