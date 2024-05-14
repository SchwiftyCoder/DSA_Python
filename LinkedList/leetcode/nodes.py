# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val: int = val
        self.next: Optional["ListNode"] = next


class DoublyListNode:
    """
    a doubly linked list can be used to implement a singly linked list by simply ignoring the .prev pointers.
    """

    def __init__(
        self,
        val: int = 0,
        prev: Optional["DoublyListNode"] = None,
        nextt: Optional["DoublyListNode"] = None,
    ) -> None:
        self.val: int = val
        self.prev: Optional["DoublyListNode"] = prev
        self.nextt: Optional["DoublyListNode"] = nextt


class DisplayLinkedList:

    def display(head: ListNode | DoublyListNode | None) -> str:
        """
        prints the elements/contents of lined lists
        """
        curr = head
        data = ""

        if isinstance(head, ListNode):
            while curr:
                data += f"{curr.val} -> "
                curr = curr.next

        elif isinstance(head, DoublyListNode):
            while curr:
                data += f"{curr.val} <--> "
                curr = curr.nextt

            data = data[:-5]
            data += "--> "

        return data + "None"
