from abc import ABC, abstractmethod 

class Authenticate(ABC):
    @abstractmethod
    def authenticate(self, password: str) -> bool:
        pass
