"""custom exception class for singly linked list"""

class EmptyQueue(Exception):
    """
        exception raised for accessing nodes with None values and .next
        Attributes: 
            message: explanation of the error
    """
    def __init__(self, message: str) -> None: 
        self.message = message

    