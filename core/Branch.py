from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from .Bank import Bank
    from ..account import Account
    from ..client import Client


class Branch:
    def __init__(self, branch_id: str, address: str, phone: str, bank: 'Bank'):
        self._branch_id = branch_id
        self._address = address
        self._phone = phone
        self._bank = bank
        self._accounts: List['Account'] = []

    @property
    def branch_id(self) -> str:
        return self._branch_id
  