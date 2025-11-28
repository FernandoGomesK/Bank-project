from pydantic import BaseModel


class AccountCreate(BaseModel):
    account_type: str
    client_id: int