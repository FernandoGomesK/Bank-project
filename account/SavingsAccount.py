from ..account import Account
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..client import Client

class SavingsAccount(Account):
    def __init__(self, account_number: str, branch_code: str, client: 'Client', balance: float = 0.0):
        super().__init__(account_number, branch_code, client, balance)