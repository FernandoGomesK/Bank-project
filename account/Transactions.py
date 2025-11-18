from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..account import Account
from datetime import datetime

class Transaction:
    def __init__(self, type: str, value: float, account: 'Account'):
        self._type = type
        self._value = value
        self._account = account
        self._date = datetime.now()


    @property
    def date(self):
        return self._date

    def get_receipt(self):
        print(f"Date: {self.date}")