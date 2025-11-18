from typing import List
from core import Branch
from client import Client
from abc import ABC, abstractmethod
from interfaces.Authenticate import Authenticate
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Transactions import Transaction


class Account(ABC, Authenticate):
    def __init__(self, number: str, password: str, client: 'Client', branch: 'Branch', balance: float = 0.0,):
        self.number = number
        self.client = client
        self.branch = branch
        self.balance = balance
        self.password = password
        self.transactions: List['Transaction'] = []

    def auntheticate(self, password: str) -> bool:
        return self._password == password