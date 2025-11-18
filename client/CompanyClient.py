from .Client import Client
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..account import Account

class CompanyClient(Client):
    def __init__(self, name: str, cnpj: str, phone: str, company_id: str):
        super().__init__(name, phone)
        self._cnpj = cnpj
        self._company_id = company_id
#getters and setters
    @property
    def cnpj(self) -> str:
        return self._cnpj
#methods
    def get_identifier(self) -> str:
        return self.cnpj
    
    def start_account(self, account: 'Account'):
            pass

    def add_account(self, account: 'Account'):
        super().add_account(account)
        