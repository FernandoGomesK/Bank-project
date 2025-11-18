class BranchNotFoundError(Exception):
    """Exception raised when a specific Branch ID/number is not found within the Bank."""
    
    def __init__(self, branch_id: str, message: str = "A Filial com o ID especificado não foi encontrada."):
        # Pass the message to the base Exception class
        super().__init__(message)
        # Store specific data related to the error
        self.branch_id = branch_id

    def __str__(self):
        # Override the string representation for a clear error message
        return f"BranchNotFoundError: {self.branch_id} - {self.args[0]}"