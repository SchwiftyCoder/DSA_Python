"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
    Input: head = [1,1,2]
    Output: [1,2]

Example 2:
    Input: head = [1,1,2,3,3]
    Output: [1,2,3]
 

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

"""

from typing import Optional
from node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        head:
            head of the linked list

        Return:
            the same linked list but with duplicates removed
        """

        curr = head 
        while curr:
            while curr.next:
                if curr.val == curr.next.val:
                    curr.next = curr.next.next
                else:
                    break
            curr = curr.next
                
        return head
            
