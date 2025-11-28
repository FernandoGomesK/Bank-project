class ClientDoesntHaveCPFException(Exception):
    def __init__(self, client_id: str):
        self.client_id = client_id
        self.message = f"Client with ID '{client_id}' does not have a CPF."
        super().__init__(self.message)
        