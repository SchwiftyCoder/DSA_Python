"""
Given a pointer to the head of a singly-linked list, print each  value from the reversed list. If the given list is empty, do not print anything.

Example

 refers to the linked list with  values 

Print the following:
3
2
1

Function Description

Complete the reversePrint function in the editor below.

reversePrint has the following parameters:

SinglyLinkedListNode pointer head: a reference to the head of the list
Prints

The  values of each node in the reversed list.

Input Format

The first line of input contains , the number of test cases.

The input of each test case is as follows:

The first line contains an integer , the number of elements in the list.
Each of the next n lines contains a data element for a list node. 
"""

from typing import Optional, List
import linkedlist_imp as ll_imp
from collections import deque

class Solution:
    def reversePrint(self, llist: Optional[ll_imp.Node]) -> None:
        """
        Method 1
        we can use a stack data 
        time: O(n) 
        space: O(n) 
        """
        items: List = []
        temp: Optional[ll_imp.Node] = llist
        while temp:
            items.append(temp.data)
            temp = temp.next
            
        print(*items[::-1], sep='\n')


    def reversePrint_v2(self, llist: Optional[ll_imp.Node]) -> None:
        """
        Method 2
        use a deque to add items 
        time: O(n)
        space: O(n)
        """

        dq = deque()
        temp = llist
        while temp:
            dq.appendleft(temp.data)
            temp = temp.next

        print(*dq, sep='\n')


    def reversePrint_v3(self, llist: Optional[ll_imp.Node]) -> None:
        """
        use recursion
            base case: head is empty
        recursive case: 
        print(llist.data)
            call function on llist.next
            and then print its value
        """
        if llist is None:
            return
        self.reversePrint_v3(llist.next)
        print(llist.data)


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
    llist = ll_imp.LinkedList()
    for item in test_cases[0]:
        llist.append(item)
    llist.display()

    # call reverse method on the head of the linked list
    sol = Solution()
    sol.reversePrint(llist.head) 
    print()
    sol.reversePrint_v2(llist.head)
    print()
    sol.reversePrint_v3(llist.head)  