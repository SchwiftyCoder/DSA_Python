"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""
from typing import Optional
from node import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """ 
        declare the node that we will be building by splicing list1 and list 2
        Args:
            list1: head node of linked list 1
            list2: head node of linked list 2

        return: 
            linked list:  the spliced list
        """

        # keeps track of the head node or beginning of the merged list
        spliced_head = ListNode()

        # keeps track of the tail or last node. for now, it points to the spliced_head
        tail = spliced_head

        #traverse the two head nodes until the shortlest length reached
        while list1 and list2:
            # determine which node to append to the spliced_head
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # update the tail to advance to the next node
            tail = tail.next

        # at the end of the traversal, append any remaining nodes to the tail node
        tail.next = list1 if list1 is not None else list2

        #return the spliced_head, skipping the dummy node at the beginning
        return spliced_head.next


                    
