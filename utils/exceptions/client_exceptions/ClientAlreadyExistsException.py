class ClientAlreadyExistsException(Exception):
    def __init__(self, client_id: str):
        self.client_id = client_id
        self.message = f"Client with ID '{client_id}' already exists."
        super().__init__(self.message)
        