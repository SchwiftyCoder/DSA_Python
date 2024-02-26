"""

1290. Convert Binary Number in a Linked List to Integer 

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

"""

from node import ListNode 

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        argument:
            head: head of the linked list

        return: 
            the decimal equivalent of the binary number
        """ 
        temp = head
        bin = ""
        while temp:
            bin += temp.val + "-"
            temp = temp.next

        # now convert the number to base 10
        print(bin)