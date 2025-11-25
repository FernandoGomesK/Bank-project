from fastapi import requests
from fastapi.responses import JSONResponse
from utils.exceptions.BranchExceptions import BranchAlreadyExistsException

async def branch_exists_handler(request: requests.Request, exc: BranchAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={
            "erro": "Erro de Validação",
            "mensagem": exc.message,
            "id_tentado": exc.branch_id},
    )