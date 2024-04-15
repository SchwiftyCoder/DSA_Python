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


from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Creates a dummy node that points to the head of the list. This simplifies edge cases, especially removals at the head.
        dummy = ListNode(next = head)
        # Set prev to this newly created dummy node. Prev will trail behind curr as we iterate.
        prev = dummy
        # Set curr to the head of the list, the current node being examined.
        curr = head
        # While there are more nodes to examine (curr is not None).
        while curr:
            # Check if the current node's value matches the target value.
            if curr.val == val:
                # If so, bypass the current node, effectively removing it by linking prev to curr's next node.
                prev.next = curr.next
            else:
                # If not, move prev forward since curr does not need to be removed.
                prev = curr
            # In either case, advance curr to the next node in the list.
            curr = curr.next
        # Return the modified list, starting from the node following the dummy. This effectively skips over any removed head element(s).
        return dummy.next


    def build_list(self, elements: List[int]) -> Optional[ListNode]:
        """
        Approach:


        Arguments:
            elements: the list to build the SLL from

        Return:
            the head of the SLL we just built
        """
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
        ([1, 2, 6, 3, 4, 5, 6], 6), # returns [1, 2, 3, 4, 5]
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
        modified_head = sol.removeElements(head, val_to_remove)
        sol.print_list(modified_head)
        print("---")