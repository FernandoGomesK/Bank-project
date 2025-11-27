class ClientAlreadyHasAccountException(Exception):
    def __init__(self, client_id: int, account_type: str):
        self.client_id = client_id
        self.account_type = account_type
        self.message = f"Client with ID {client_id} already has {account_type} account."
        super().__init__(self.message)