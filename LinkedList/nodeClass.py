from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):

    def __init__(self, data: T) -> None:
        """ create a node wth data and points to none"""
        self._data = data
        self._next = None 

    def get_data(self) -> T:
        """ return the data being held in the node"""
        return self._data
    
    def set_data(self, data: T) -> None:
        self._data = data

    def set_next(self, next: Optional['Node[T]']) -> None:
        """optional here means the method can accept either a Node object or None value"""
        self._next = next

    def get_next(self) -> Optional['Node[T]']:
        return self._next

    def __str__(self) -> str:
        """override functoin that prints the data of a node instead of the memory address"""
        return str(self._data)
    
    