"""queue implemnetation using singly linked list"""

from typing import TypeVar, Generic
from SLL_implementation import SinglyLinkedList
from sll_exceptions import EmptyQueue
T = TypeVar("T")

class QueueUsingSLL(Generic[T]):
    """
        uses a singly linked list to implement a queue
        we do not have any restriction on the queue capacity
    """

    def __init__(self) -> None:
        """uses a singly linked list to implement a queue"""
        self._queue = SinglyLinkedList() 

    def enqueue(self, element: T) -> None:
        """
            adds an element to the rear of the queue. for a sll, inserts last
        """
        self._queue.add_last(element)

    def dequeue(self) -> T:
        """
            removes an element from the front of the queue
            returns None if queue is empty else returns the removed element    
        """
        front = None
        try:
            front = self._queue.getHead()
            self._queue.removeHead()
        except EmptyQueue:
            print("Queue is empty")

        return front

    def clear(self) -> None:
        """
            removes all elements from the queue
        """
        self._queue.clear()

    def __len__(self) -> int:
        """
            returns the size of the queue
        """
        return self._queue.size()

    def __str__(self) -> str:
        """
            displays all the elements of the queue
        """
        queue = self._queue.__str__()
        queue = queue.replace(" -> None", "")
        return queue

# test cases: only runs in the current script
if __name__ == "__main__":
    queue_sll = QueueUsingSLL[str]()
    queue_sll.dequeue()
    queue_sll.enqueue("abc")
    queue_sll.enqueue("bac")
    print(queue_sll)
    queue_sll.enqueue("cba")
    print(queue_sll)
    queue_sll.dequeue()
    print(queue_sll)
    queue_sll.enqueue("xzy")
    queue_sll.enqueue("zyx")
    print(queue_sll)
    queue_sll.dequeue()
    queue_sll.dequeue()
    queue_sll.dequeue()
    print(queue_sll)
    queue_sll.dequeue()
    print(queue_sll)
    queue_sll.dequeue()
    print(queue_sll)