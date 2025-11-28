from fastapi import Request
from fastapi.responses import JSONResponse
from utils.exceptions.BranchExceptions import BranchAlreadyExistsException
from utils.exceptions.client_exceptions import (ClientAlreadyExistsException, ClientDoesntHaveCNPJException, 
                                                ClientDoesntHaveCPFException, BranchDoesntExistException)
from utils.exceptions.auth_exceptions.InvalidCredentialsException import InvalidCredentialsException
from utils.exceptions.Account_exceptions import ClientDoesntExistException, ClientAlreadyHasAccountException
from utils.exceptions.general_exceptions import InvalidNumberException

async def branch_exists_handler(request: Request, exc: BranchAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={
            "erro": "Erro de Validação",
            "mensagem": exc.message,
            "id_tentado": exc.branch_id},
    )

async def client_exists_handler(request: Request, exc: ClientAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={
            "erro": "Erro de Validação",
            "mensagem": exc.message,
            "id_tentado": exc.client_id},
    )
    
async def client_missing_cpf_handler(request: Request, exc: ClientDoesntHaveCPFException):
    return JSONResponse(
        status_code=400,
        content={
            "erro": "Erro de Validação",
            "mensagem": exc.message,
            "id_tentado": exc.client_id},
    )

async def client_missing_cnpj_handler(request: Request, exc: ClientDoesntHaveCNPJException):
    return JSONResponse(
        status_code=400,
        content={
            "erro": "Erro de Validação",
            "mensagem": exc.message,
            "id_tentado": exc.client_id},
    )
    
async def branch_doesnt_exist_handler(request: Request, exc: BranchDoesntExistException):
    return JSONResponse(
        status_code=404,
        content={
            "erro": "Recurso Não Encontrado",
            "mensagem": exc.message,
            "id_tentado": exc.branch_id},
    )
    
    
async def invalid_credentials_handler(request: Request, exc: InvalidCredentialsException):
    return JSONResponse(
        status_code=401,
        content={
            "erro": "Credenciais Inválidas",
            "mensagem": exc.message},
    )
    
    
async def client_doesnt_exist_handler(request: Request, exc: ClientDoesntExistException):
    return JSONResponse(
        status_code=404,
        content={
            "erro": "Recurso Não Encontrado",
            "mensagem": exc.message,
            "id_tentado": exc.client_id},
    )
    
    
async def client_already_has_account_handler(request: Request, exc: ClientAlreadyHasAccountException):
    return JSONResponse(
        status_code=400,
        content={
            "erro": "Erro de Validação",
            "mensagem": exc.message,
            "id_tentado": exc.client_id},
    )

async def invalid_number_handler(request: Request, exc: InvalidNumberException):
    return JSONResponse(
        status_code=422,
        content={"erro": "Formato Inválido", "mensagem": exc.message}
    )