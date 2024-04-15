""" 

Function Description

Complete the mergeLists function in the editor below.

mergeLists has the following parameters:

SinglyLinkedListNode pointer headA: a reference to the head of a list
SinglyLinkedListNode pointer headB: a reference to the head of a list
Returns

SinglyLinkedListNode pointer: a reference to the head of the merged list
Input Format

The first line contains an integer , the number of test cases.

The format for each test case is as follows:

The first line contains an integer , the length of the first linked list.
The next  lines contain an integer each, the elements of the linked list.
The next line contains an integer , the length of the second linked list.
The next  lines contain an integer each, the elements of the second linked list.

"""

from node import Node
from typing import Optional, List
from linkedlist_imp import LinkedList

class Solution:

    def mergeLists(self, head1: List, head2: List) -> Optional[List]:
        """
        Approach: 
        variables:
            p1 to track head1
            p2 to track head2
            merge to store the merge of head1 and head2. initially set to a dummy node
            tail to keep track of where to add nodes to the merge

            1. while both p1 and p2 are not empty
            2. if p1 data smaller than p2 data:
                    point tail next node to p1
                    advance p1 to next node
                    else:
                    point tail next node to p2
                    advance p2 to next node
            3. advance tail to next node at all costs

            4. while loop ends: add any remaining nodes from wither p1 or p2
            5. return merge.next
            
        
        
        """

        curr1 = head1
        curr2 = head2

        mergedList = Node('')
        tail = mergedList # stores a reference to the last node of the merged list

        while curr1 and curr2:
            # add the node with the smallest data
            if curr1.data < curr2.data:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next # move on the next node in merge

        # add any remaining nodes from either curr1/2
        while curr1:
            tail.next = curr1
            curr1 = curr1.next
            tail = tail.next

        while curr2:
            tail.next = curr2
            curr2 = curr2.next
            tail = tail.next


        return mergedList.next

        
    

# TEST CASES
if __name__ == "__main__":
    print("hola")