class Empty(Exception):
    
    """exception raised when trying to access element from an empty queue"""
    def __init__(self, errorMessage="Queue is empty") -> None:
        self.errorMessage = errorMessage
        super().__init__(self.errorMessage)


class Full(Exception):

    """exception raised when trying to access add element to a full queue"""
    def __init__(self, errorMessage="Queue is full") -> None:
        self.errorMessage = errorMessage
        super().__init__(self.errorMessage)