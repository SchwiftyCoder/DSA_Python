from typing import TypeVar

T = TypeVar("T")  # generic type T
from queueExceptions import Full, Empty


class ArrayQueue:
    defaultCapacity = 5  # class level variable to set a global size of all queue objects

    def __init__(self) -> None:
        """create a queue object with 5 default capacity, front and rear set to an initial value of 0"""
        self._data = [None] * ArrayQueue.defaultCapacity
        self._front = 0  # keep track of the index of the first/next element in the queue
        self._size = 0  # also called rear, used to keep track of the number of non None values

    def __len__(self) -> int:
        """returns the size of the queue. this also refers to the index of the current enqueue operation"""
        return self._size

    def isEmpty(self) -> bool:
        """returns true if queue is empty"""
        return self._size == 0

    def enqueue(self, element) -> None:
        """add an element to the queue else raise exception if queue is full"""
        if self._size == ArrayQueue.defaultCapacity: # halts all queue operations 
            # self._size = 0 # is wrong because it simply overwrites the next enqueue operation
            raise Full()
        
        # proper circular buffer/array operation: wraps the index if it exceeds the queue capacity
        rear = (self._front + self._size) % ArrayQueue.defaultCapacity # computes the next position to enqueue element
        self._data[rear] = element
        self._size += 1

    def dequeue(self):
        """removes an element from the front of the queue"""
        if self.isEmpty():
            raise Empty()
        
        # proceed with dequeue operation

    def __str__(self) -> str:
        """
            display only elements that are not None, similar to Java toString()
            the list comprehension ensures that only non None values are displayed
        """
        queueWithNoneValues = [e for e in self._data if e != None]
        return f"{queueWithNoneValues}"
    
if __name__ == "__main__":
    q = ArrayQueue()
    print(q.isEmpty())
    q.enqueue(23)
    print(q)
    print(q.isEmpty())
    q.enqueue(-1)
    q.enqueue(100)
    q.enqueue(0)
    print(q)
    print(q.isEmpty())
    q.enqueue(234)
    print(q) 

    # queue is at capacity, exception raised with an message
    # q.enqueue(809)

    # same enqueue operation but exception caught
    try:
        q.enqueue(809)
    except Full as e:
        print(e)
