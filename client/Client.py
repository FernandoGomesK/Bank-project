from abc import ABC, abstractmethod

class Client:
    def __init__(self, name: str, cpf: str, phone: str):
        self.name = name
        self.cpf = cpf
        self.phone = phone