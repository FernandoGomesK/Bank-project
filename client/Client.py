from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from ..account import Account

class Client(ABC):
    def __init__(self, name: str, phone: str):
        self._name = name
        self._phone = phone
        self._accounts: List['Account'] = []

    @abstractmethod
    def get_identifier(self) -> str:
        pass
        
    @abstractmethod
    def start_account(self, account: 'Account'):
        pass
    
    
    def add_account(self, account: 'Account'):
        self._accounts.append(account)