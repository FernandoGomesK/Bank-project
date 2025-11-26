from fastapi import Request
from fastapi.responses import JSONResponse
from utils.exceptions.BranchExceptions import BranchAlreadyExistsException
from utils.exceptions.client_exceptions import ClientAlreadyExistsException, ClientDoesntHaveCNPJException, ClientDoesntHaveCPFException

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