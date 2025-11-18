from typing import List
from core import Branch
from client import Client
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, number: str, password: str, client: 'Client', branch: 'Branch', balance: float = 0.0,):
        self.number = number
        self.client = client
        self.branch = branch
        self.balance = balance
        self.password = password
        self.transactions: List = []