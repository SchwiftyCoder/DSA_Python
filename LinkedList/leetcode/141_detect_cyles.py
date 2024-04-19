"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



"""

from typing import Optional
from node import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        use two pointers fast and slow
        slow = 1 node per loop
        fast = two nodes per loop
        make a move on both pointers and then check if their ids (or ==) are the same
        if slow and fast occupy the same meory, then there is a cycle
        """

        fast: Optional[ListNode] = head
        slow: Optional[ListNode] = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow: # fast == slow: # id(fast) == id(slow): 
                print(f"same memory: \nfast: {id(fast)}, \nslow: {id(slow)}\n")
                return True
            print(f"different memory: \nfast: {id(fast)}, \nslow: {id(slow)}\n")

        return False
    

if __name__ == "__main__":
    sol = Solution()
    node_a = ListNode(1)
    node_b = ListNode(2)
    node_c = ListNode(3)

    check_cycle = lambda x: print(f"cycle is detected!") if x else print(f"no cycles")

    # create linekd list: no cycles
    node_a.next = node_b # 1 -> 2
    node_b.next = node_c # 2 -> 3

    check_cycle(sol.hasCycle(node_a))

    # create linekd list: cycles
    node_a.next = node_b # 1 -> 2
    node_b.next = node_a # 2 -> 1

    check_cycle(sol.hasCycle(node_a))

