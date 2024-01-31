"""
implementation of Stack Using SLL
data type here is generic, obtained at runtime
our stack needs to inherit from the base class SinglyLinkedList and 
"""

from nodeClass import Node
from typing import TypeVar, Generic, Optional
from SLL_implementation import SinglyLinkedList
T = TypeVar('T')

class StackUsingSLL(Generic[T]):

    def __init__(self) -> None: 
        """creates a new stack object using a sll"""
        self._stack = SinglyLinkedList[T]()

    def __len__(self) -> int:
        """overrides the build in len() to return the length of the stack"""
        return self._stack.size()

    def isEmpty(self) -> bool:
        """ checks whether stack is empty"""
        return self._stack.isEmpty()

    def push(self, element: T) -> None:
        """adds an element to the top of the stack"""
        self._stack.add_first(element)

    def pop(self) -> T:
        """
            returns None if stack is empty
            else
            removes and returns the top element in the stack, 
        """
        if self._stack.isEmpty():
            return None
        return self._stack.removeHead().get_data()

    def peek(self) -> T:
        """returns but does not remove the top of the stack"""
        if self._stack.isEmpty():
            return None
        return self._stack.getHead()

    def __str__(self) -> str: 
        """
            returns a string representation of the stack
        """
        return self._stack.__str__()


    def clear(self) -> None:
        self._stack.clear()


# TEST CASES: only executed in the current script
if __name__ == "__main__":
    """all methods test cases"""
    stack_sll = StackUsingSLL[int]()

    # testig the empty stack
    print(len(stack_sll)) 
    print(stack_sll)
    print(stack_sll.isEmpty())
    print(stack_sll.peek())
    print(stack_sll.pop())

    # add elements to the stack
    stack_sll.push(23)
    stack_sll.push(124)
    stack_sll.push(9000)

    print(stack_sll)

    # testig the non-empty stack
    print(len(stack_sll)) 
    print(stack_sll.isEmpty())
    # print(stack_sll.peek())
    print(stack_sll.pop()) 
    print(len(stack_sll))

    print(stack_sll)

    stack_sll.clear()

    # testig the empty stack
    print(len(stack_sll)) 
    print(stack_sll)
    print(stack_sll.isEmpty())
    print(stack_sll.peek())
    print(stack_sll.pop())



