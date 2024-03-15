"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from node import ListNode
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        if head is None:
            return None
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next

        reversed_head = ListNode()
        start = reversed_head
        while stack:
            start.next = ListNode(stack.pop())
            start = start.next

        return reversed_head.next
