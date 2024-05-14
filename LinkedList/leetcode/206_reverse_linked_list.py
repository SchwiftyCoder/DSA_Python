"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from nodes import ListNode
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

    def reverseList_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        input:
            head of singly linked list

        outpt:
            the head of the same list but revered, tail becomes head and vice versa

        Approach:
            set a prev node to None
            set curr node to head
            while current node is not empty:
                save the next node after curr
                set the next node after curr to prev
                set the prev node to curr
                set the curr node to the next node saved prior

            return the prev node since it becomes the head of the new linked list

        """

        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head

        while curr:
            nextNode: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev
