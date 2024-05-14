"""

Given a reference to the head of a doubly-linked list and an integer, , create a new DoublyLinkedListNode object having data value  and insert it at the proper location to maintain the sort.

Example

 refers to the list 

Return a reference to the new list: .

Function Description

Complete the sortedInsert function in the editor below.

sortedInsert has two parameters:

DoublyLinkedListNode pointer head: a reference to the head of a doubly-linked list

int data: An integer denoting the value of the  field for the DoublyLinkedListNode you must insert into the list.

Returns

DoublyLinkedListNode pointer: a reference to the head of the list
Note: Recall that an empty list (i.e., where ) and a list with one element are sorted lists.

Input Format

The first line contains an integer , the number of test cases.

Each of the test case is in the following format:

The first line contains an integer , the number of elements in the linked list.
Each of the next  lines contains an integer, the data for each node of the linked list.
The last line contains an integer, , which needs to be inserted into the sorted doubly-linked list.
Constraints

Sample Input

STDIN   Function
-----   --------
1       t = 1
4       n = 4
1       node data values = 1, 3, 4, 10
3
4
10
5       data = 5
Sample Output

1 3 4 5 10
Explanation

The initial doubly linked list is:  .

The doubly linked list after insertion is: 

"""

from typing import Optional, List
from nodes import DoublyListNode

class Solution:

    def sortedInsert(self, llist: Optional[DoublyListNode], data: int):
        """
        input: 
            1. head of doubly linked list
            2. data to insert into list
            
        output:
            the original sorted linked list with the data inserted correctly
            
        Approach:
        create a new node with prev and next pinting to None
        
            Scenario 1:
                linked list head is empty
                    return the newly created node
                    
            Scenario 2:
                node to insert has its data smaller than the data at the head
                    1. point the prev of the head to the newly created node next.
                    2. return the newly created node
            
            Scenario 3:
                node to insert is somewhere in the middle of the linked list
                    1. navigate to the node before and after 
                    2. point the .next of the before node to new node .prev
                    3. point the .next of the new node to the .prev of the after node
                    3. return the head of the linked list
                    
            Scenario 4:
                node to insert has its data greater than all other nodes
                    1. point the .next of the tail node to the .prev of the new node
                    2. return the head fo the linked list
                    
                
        """

        newNode = DoublyListNode(data)

        # llist is empty
        if llist is None:
            return newNode
        
        # insert at the beginning
        if data < llist.val:
            newNode.nextt = llist
            llist.prev = newNode
            return newNode
        
        # data to insert is somewhere in the middle
        curr = llist
        while curr and curr.nextt:
            nextNode = curr.nextt
            if data > curr.val and data < nextNode.val:
                curr.nextt = newNode
                nextNode.prev = newNode
                newNode.prev = curr
                newNode.nextt = nextNode
                return llist
            curr = curr.nextt

        # data to insert is greater than all the nodes 
        print(f"\nlast node: {curr.val}\n", end='\n')
        curr.nextt = newNode
        newNode.prev = llist 

        return llist

        
                

# test cases
if __name__ == '__main__':

    def printDoublyList(head: Optional[DoublyListNode]) -> str:
        curr = head
        # print(f"None <-- ", end='')
        while curr:
            print(f"{curr.val} <--> ", end='')
            curr = curr.nextt

        # print(f"None", end='\n\n')
        print()

    # create the individual nodes
    node_1 = DoublyListNode(1)
    node_2 = DoublyListNode(2)
    node_3 = DoublyListNode(3)

    # build the links between them
    node_1.nextt = node_2
    node_2.prev = node_1

    node_2.nextt = node_3
    node_3.prev = node_2


    printDoublyList(node_1)

    # test code 

    sol = Solution()

    # doubly linked list is empty, inserting 3
    # head = DoublyListNode()
    # data = 3
    # head = sol.sortedInsert(head, data)
    # printDoublyList(head)

    # doubly linke dlist is not empty, inseting 4
    head = node_1
    data = 4
    head = sol.sortedInsert(head, data)
    
    printDoublyList(head)


    

