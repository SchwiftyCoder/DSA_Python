"""

Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. That is, change the next and prev pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

Note: The head node might be NULL to indicate that the list is empty.

Function Description

Complete the reverse function in the editor below.

reverse has the following parameter(s):

DoublyLinkedListNode head: a reference to the head of a DoublyLinkedList
Returns
- DoublyLinkedListNode: a reference to the head of the reversed list

Input Format

The first line contains an integer , the number of test cases.

Each test case is of the following format:

The first line contains an integer , the number of elements in the linked list.
The next  lines contain an integer each denoting an element of the linked list.
Constraints

Output Format

Return a reference to the head of your reversed list. The provided code will print the reverse array as a one line of space-separated integers for each test case.


"""

from nodes import DoublyListNode, DisplayLinkedList
from typing import Optional

class Solution:

    def reverse_doubly_list(self, llist: Optional[DoublyListNode]) -> Optional[DoublyListNode]:
        """
        input: 
            head of doubly linkedlist, may be empty
        
        output:
            the head of the doubly linedlist but reversed

        Approach:
            prev = None
            curr = head
            while curr is not empty:
                save the next node after curr

                point the .prev of the curr node to the next node saved prior 
                point the .next of the curr node to prev  

                set prev to the current node 
                set the current node to next node 
    
            return prev 
        """

        prev = None
        curr = llist

        while curr:
            nextNode = curr.nextt

            curr.prev = nextNode
            curr.nextt = prev

            prev = curr
            curr = nextNode

        return prev
    

# test
if __name__ == '__main__':

    # individual nodes
    node_1 = DoublyListNode(1)
    node_2 = DoublyListNode(2)
    node_3 = DoublyListNode(3)

    # linking
    node_1.nextt = node_2
    node_2.prev = node_1
    node_2.nextt = node_3
    node_3.prev = node_2

    # display nodes
    data = DisplayLinkedList.display(node_1)
    print(data)

    # reverse the nodes and then display
    sol = Solution()
    node_1_reversed = sol.reverse_doubly_list(node_1) 
    data = DisplayLinkedList.display(node_1_reversed)
    print(data)
