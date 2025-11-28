class BranchAlreadyExistsException(Exception):
    """Exception raised when trying to create a branch that already exists."""
    def __init__(self, branch_id: str):
        self.branch_id = branch_id
        self.message = f"Branch with ID '{self.branch_id}' already exists."
        super().__init__(self.message)