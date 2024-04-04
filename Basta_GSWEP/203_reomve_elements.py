"""
203. Remove Linked List Elements 
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 
Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev, curr = dummy, head 
        while curr:
            next_node = curr.next
            if curr.val == val:
                prev.next = next_node
            else:
                prev = curr

            curr = next_node

        return dummy.next


    def build_list(self, elements):
        head = ListNode(elements[0]) if elements else None
        current = head
        for element in elements[1:]:
            current.next = ListNode(element)
            current = current.next
        return head

    def print_list(self, head):
        elements = []
        current = head
        while current:
            elements.append(current.val)
            current = current.next
        print("List:", elements)

if __name__ == "__main__":
    tests = [
        ([1, 2, 6, 3, 4, 5, 6], 6),
        ([], 1),
        ([7, 7, 7, 7], 7),
        ([1, 2, 3, 4, 5], 3),
        ([6, 6, 6, 6, 6], 6),
        ([1, 2, 3, 4, 5], 10)
    ]

    sol = Solution()
    
    for test in tests:
        input_list, val_to_remove = test
        head = sol.build_list(input_list)
        print("Original:", input_list, "Remove:", val_to_remove)
        solution = Solution()
        modified_head = solution.removeElements(head, val_to_remove)
        sol.print_list(modified_head)
        print("---")