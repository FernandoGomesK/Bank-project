from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from .Branch import Branch

from .Branch import Branch
from utils.exceptions import InvalidBranchInstanceError

class Bank:
    def __init__(self, name: str, cnpj, address: str, phone: str):
        self._name = name
        self._cnpj = cnpj
        self._address = address  
        self._phone = phone
        self._branches: List['Branch'] = []
    
    def add_branch(self, branch: 'Branch'):
        if not isinstance(branch, Branch):
            raise InvalidBranchInstanceError(type(branch).__name__)
        self._branches.append(branch)

    def show_branches(self) -> List['Branch']:
        return self._branches

