"""
160. Intersection of Two Linked Lists 

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.



e.g.
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
Example 2:

Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
from node import ListNode
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        1. input: 
            heads of 2 linked lists
        2. output: 
            the intersecoin node
        3. approach: 
            a. get the length of the linked lists.
            b. find the shortest lined list
            c. iterate through the two linekdlists simultaneoulsy using the shortest node as the starting point.
                e.gif  len(l1) = 8
                       len(l2) = 5
                       then shortest = l2
                       iterate through l2 starting with head node
                       iterate through l1 starting with the (8-5)th node, i.e the 3rd node
            d. compare both nodes to see if they point to the same memory location and return that node
            e. return None if while loop ends and nodes do not merge

        4. corner cases: 
            one of heads are None,  return None
        5. test acses: 
            l1: [3, 2, 4, 9]
            l2: [90, 87, 4, 9, 90, 12]
                none of the linkedlists are empty
                len_l1 = 4
                len_l2 = 6
                shorter linkedlist: l1
                node to start iterating through the longer list: len_l2 - len_l1

        6. algorithm analysis:
            runtime: 
                     O(n + m) initial pass
                     O(k) second pass
                     n and m are the length of the two linkedlists
                     k is the length of the shortest one: either n or m
            
                     
            space: 
                    O(1 + 1 + 1)
                    the pointer to the 2 head nodes
                    another pointer to the starting point of the longer node

        
        """

        def printlist(l):
            c = l
            while c:
                print(f"{c.val} -> ", end='')
                c = c.next

            print(f" None", end='\n')

        len1 = 0
        len2 = 0

        curr1 = headA
        curr2 = headB

        # find the lengths of the two linked lists
        while curr1 or curr2:
            if curr1:
                len1 += 1
                curr1 = curr1.next
            if curr2:
                len2 += 1
                curr2 = curr2.next

        if len1 == len2 and headA.val is not headB.val:
            return None

        print(f"len_h1: {len1}\nlen_h2: {len2}")

        # identify the shortest and longest linkedlists
        longestLL: Optional[ListNode] = headA if len1 > len2 else headB  
        shortestLL: Optional[ListNode] = headA if len1 < len2 else headB 

        print(f"longest: ")
        printlist(longestLL)
        print(f"shortest: ")
        printlist(shortestLL)

        # find the []abs(len1 - len2)]th node in the longest to start traversing from
        longest_curr: Optional[ListNode] = longestLL
        for _ in range(abs(len1 - len2)):
            longest_curr = longest_curr.next 

        # begin parallel traversal between both linkedlists
        curr_sh: Optional[ListNode] = shortestLL
        curr_lg: Optional[ListNode] = longest_curr
        
        print(f"longest: {printlist(curr_sh)}")
        print(f"shortest: {printlist(curr_lg)}")

        while curr_sh and curr_lg:
            print(f"sh: {id(curr_sh)}")
            print(f"lg: {id(curr_lg)}\n")
            # if curr_sh is curr_lg: 
            #     print(curr_sh.val)
            #     return curr_sh
            curr_sh = curr_sh.next
            curr_lg = curr_lg.next
        
        return None


if __name__ == '__main__':
    
    shared = ListNode(4, ListNode(5, ListNode(4)))  # This node and its next will be shared by both lists.

    list1 = ListNode(2, ListNode(2, shared))  # List1 joins the shared part at '4'
    
    list2 = ListNode(2, ListNode(2, shared))  # List2 also joins the shared part at '4'

    sol = Solution()
    # print(sol.getIntersectionNode(list1, list2))

    # Create the shared part of the lists
    node_shared_2 = ListNode(5)
    node_shared_1 = ListNode(7, node_shared_2)

    # Create Linked List 1
    node1_2 = ListNode(2, node_shared_1)
    node1_1 = ListNode(1, node1_2)

    # Create Linked List 2
    node2_3 = ListNode(6, node_shared_1)
    node2_2 = ListNode(4, node2_3)
    node2_1 = ListNode(3, node2_2)

    def printlist(l):
            c = l
            while c:
                print(f"{c.val} -> ", end='')
                c = c.next

            print(f" None", end='\n\n')

    printlist(node1_1)
    printlist(node2_1)

    a = node1_1
    b = node2_1
    flag_a = 1
    flag_b = 1
    while a and b: 
        if a is b:
            print(f"merge point node: {a.val}")
            break
        a = a.next
        b = b.next
        if a is None and flag_a:
            a = node2_1
            flag_a = 0
        if b is None and flag_b:
            b = node1_1
            flag_b = 0

    

    # Now node1_1 is the head of the first linked list
    # And node2_1 is the head of the second linked list
    # Both lists will intersect at node_shared_1 (value 7) and continue together to node_shared_2 (value 5)



