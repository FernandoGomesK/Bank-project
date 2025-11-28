# main.py
from fastapi import FastAPI
from config.database import engine, Base
from routes import client_routes, branch_routes, account_routes, auth_routes

from utils.exceptions.Registration import register_exception_handlers


Base.metadata.create_all(bind=engine)

app = FastAPI()

register_exception_handlers(app)

@app.get("/")
def read_root():
    return {"mensagem": "O Banco Beto está ON! Acesse /docs para usar."}

# 2. Inclui as rotas do branch_routes
app.include_router(branch_routes.router)
app.include_router(client_routes.router)
app.include_router(account_routes.router)
app.include_router(auth_routes.router)