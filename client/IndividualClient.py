from .Client import Client
from .Client import Client
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..account import Account


class IndividualClient(Client):
    def __init__(self, name: str, cpf: str, phone: str, date_of_birth: str):
        super().__init__(name, phone)
        self._cpf = cpf
        self._date_of_birth = date_of_birth

#getters and setters
    @property
    def cpf(self) -> str:
        return self._cpf
# Methods

    def get_identifier(self) -> str:
        return self.cpf
    
    def start_account(self, account: 'Account'):
            pass

    def add_account(self, account: 'Account'):
        super().add_account(account)
        