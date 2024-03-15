"""
Stack Method	Realization with Python List
--------------------------------------------
S.push(e)	    L.append(e)
S.pop()	        L.pop()
S.top()	        L[-1]
S.is_empty()	len(L) == 0
len(S)	        len(L)

"""

import stackExceptions
"""include type hints"""
from typing import List, TypeVar
T = TypeVar('T') # generic type T

class ArrayStack:
    """
        LIFO Stack implementation using a Python List as underlying storage 
    """

    # constructor to create new stack objects
    def __init__(self):
        """Create an empty stack"""
        self._data = []                 # private list instance
        

    def __len__(self) -> int:
        """returns the number of elements in the stack"""
        return len(self._data)
    
    def isEmpty(self) -> bool:
        """returns true if stack is empty else false"""
        return len(self._data) == 0
    
    def push(self, element) -> None:
        """adds an element to the top of the stack"""
        self._data.append(element)

    def pop(self) -> T:
        """remove and return top/last element from the stack
            raise empty exception if stack is empty    
        """
        if self.isEmpty():
            raise stackExceptions.Empty("Stack is Empty")
        return self._data.pop()
    
    def top(self) -> T:
        """return top element without removing it
            raise empty exception if stack is empty
        """
        if self.isEmpty():
            raise stackExceptions.Empty("Stack is Empty")
        return self._data[-1]
    
    def __str__(self) -> str:
        return f"{self._data}"







