class BranchDoesntExistException(Exception):
    def __init__(self, branch_id: int):
        self.branch_id = branch_id
        self.message = f"Branch with ID {branch_id} does not exist."
        super().__init__(self.message)