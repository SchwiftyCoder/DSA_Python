"""
Given a pointer to the head of a linked list and a specific position, determine the data value at that position. Count backwards from the tail node. The tail is at postion 0, its parent is at 1 and so on.

Example
 refers to 

Each of the data values matches its distance from the tail. The value  is at the desired position.

Function Description

Complete the getNode function in the editor below.

getNode has the following parameters:

SinglyLinkedListNode pointer head: refers to the head of the list
int positionFromTail: the item to retrieve
Returns

int: the value at the desired position
"""
from typing import Optional, List 
class Solution:

    def getNode(llist: Optional[list], positionFromTail: int):
        """
        Naive approach: convert linked list to array and return the ith positoin from the reversed array

        Time complexity:
            appending to list: O(n)
            reversing list: o(n)

        Space complexity: 
            list size: O(n)

            waaayy too expensive!
        """

        curr: Optional[List] = llist
        llist_to_list: List = []
        while curr:
            llist_to_list.append(curr.data)
            curr = curr.next

        return llist_to_list[::-1][positionFromTail]
    
    def getNode_v2(llist, positionFromTail):
        """
        two passes through the linked list
        1st pass: to find the length of the linked list
        2nd pass: find the ith node data we are after from the tail
        use the formula: (len-positoinFromTail)

        requires only O(2n) time complexity and constant space
        """

        curr = llist
        llist_len = 0
        while curr:
            llist_len += 1
            curr = curr.next

        curr2 = llist
        for _ in range((llist_len - 1) - positionFromTail):
            curr2 = curr2.next

        return curr2.data