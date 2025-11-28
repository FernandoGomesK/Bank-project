class InvalidNumberException(Exception):
    """Exception raised for invalid number inputs."""

    def __init__(self, message="The provided number is invalid."):
        self.message = message
        super().__init__(self.message)