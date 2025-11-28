class InvalidCredentialsException(Exception):
    """Exception raised for invalid authentication credentials."""
    
    def __init__(self, message="Invalid credentials provided."):
        self.message = message
        super().__init__(self.message)