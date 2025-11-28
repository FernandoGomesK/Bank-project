class ClientDoesntExistException(Exception):
    def __init__(self, client_id: int):
        self.client_id = client_id
        self.message = f"Client with ID {self.client_id} does not exist."
        super().__init__(self.message)