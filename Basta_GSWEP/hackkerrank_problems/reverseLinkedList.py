"""
Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.

Example
 references the list 

Manipulate the  pointers of each node in place and return , now referencing the head of the list .

Function Description

Complete the reverse function in the editor below.

reverse has the following parameter:

SinglyLinkedListNode pointer head: a reference to the head of a list
Returns

SinglyLinkedListNode pointer: a reference to the head of the reversed list
Input Format

The first line contains an integer , the number of test cases.

Each test case has the following format:

The first line contains an integer , the number of elements in the linked list.
Each of the next  lines contains an integer, the  values of the elements in the linked list.

"""

from node import Node
from typing import Optional, List
from linkedlist_imp import LinkedList

class Solution: 

    def reverse(self, llist: Optional['Node']) -> Optional['Node']:
        """
        Arguments: 
            llist:  INTEGER_SINGLY_LINKED_LIST llist as parameter.
                    may be empty/None

        Returns:
            an INTEGER_SINGLY_LINKED_LIST or None of llsit is empty


        Approach:
        use 2 pointers:
            prev = initial value is None 
            curr = initial value is head and used to traverse the linked list 

            while curr not empty:
                # store the next node after current
                # set the next node after current to the prev node i.e. reversing
                # update the prev to now point to the current node
                # move on to the next node in the list


            return prev


        """ 
        curr = llist
        prev = None
        while curr: 
            next_temp_node = curr.next 
            curr.next = prev
            prev = curr
            curr = next_temp_node

        while prev:
            print(f"{prev.data}, ", end='')
            prev = prev.next

        return prev
    
if __name__ == '__main__':
    test_cases: List = [
        (1, 2, 6, 3, 4, 5, 6, 6),
        (1),
        (),
        (7, 7, 7, 7, 7),
        (1, 2, 3, 4, 5, 3),
        (6, 6, 6, 6, 6, 6),
        (1, 2, 3, 4, 5, 10)
    ]

    # build and display linkedlist
    llist = LinkedList()
    for item in test_cases[0]:
        llist.append(item) 

    # call reverse method on the head of the linked list
    sol = Solution()
    sol.reverse(llist.head) 
            

