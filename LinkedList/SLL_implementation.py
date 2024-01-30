from nodeClass import Node
from typing import TypeVar, Generic, Optional
T = TypeVar('T')

class SinglyLinkedList(Generic[T]):

    def __init__(self) -> None:
        """ initially, both the head and tail do not point to any nodes and thus empty/none value"""
        self._head = None
        self._tail = None
        self._size = 0

    def add_first(self, data: T) -> None:
        """
        1. create a new node with data, [points to nothig yet]  
        2. if head is none, update the tail to new node 
        3. point the next of the new node to head
        4. update the head node next to new node
        5. increase the node count by 1

        """
        newNode = Node(data)
        if self._head == None:
            self._tail = newNode
        newNode._next = self._head
        self._head = newNode
        self._size += 1

    def add_last(self, data: T) -> None:
        """add an element as the tail of the sll
        Notes:
            if head is empty, call add_first
            else point the next of the current tail to the new node and 
            update the tail to the new node
        """
        newNode = Node(data)
        if self._head == None:
            """if the list is empty, adding to the end is equivalent to adding to the beginning."""
            self.add_first(data)
        else: 
            """point the tail next to the new node and update the tail reference to this new node"""
            self._tail._next = newNode
            self._tail = newNode
            self._size += 1

    def removeHead(self):
        """ 
        update and return the head node to the next element
        if the sll is empty after head removal, update the tail reference to None
        """
        head = self._head 
        if self._head != None:
            self._head = self._head.get_next()
            self._size -= 1
            if self.isEmpty():
                self._tail = None
        
        return head
    
    def removeTail(self):
        """
        remove and return the tail node
        head node must not be empty
        we need to traverse the sll to the node before tail, 
            while keeping track of the previous node
        update the tail refrence to the new last element
        """
        tail = self._tail
        print(f"prev. tail: {tail}")

        """there is only one element in the sll"""
        if self._head.get_next() == None:
            self._head, self._tail = None, None

        """there is more than 1 element"""
        if self._head:
            tempNode = self._head
            lastNode = self._head
            while tempNode.get_next():
                lastNode = tempNode
                tempNode = tempNode.get_next()
            lastNode.set_next(None) # set the last but one node to None
            self._tail = lastNode  # update the tail reference
            self._size -= 1
        
        return tail

    
    def removeElement(self, element: T) -> T:
        """check if an element exists in the sll and return/remove it"""
        index = self.search(element) # get the index of the element if exists
        node = None
        if index == -1:
            print(f"\"{element}\" not found")
        elif index == 0:
            """remove head"""
            self.removeHead()
        elif index == self._size-1:
            """remove head"""
            self.removeTail()
        else:
            """node to remove must be in the middle somewhere at position n"""
            position = 1 
            prevNode = self._head
            postNode = None
            """get the node before the one to delete"""
            while position < index:
                position += 1
                prevNode = prevNode.get_next()
            """get the node after the one to delete"""
            node = prevNode.get_next()
            if position == (index):
                postNode = prevNode.get_next().get_next()
            
            if __name__ == "__main__":
                print(f"position: {position}\nprev node: {prevNode}\nnext node: {postNode}\nNode to delete: {node}")
            """connect the previous node to the next node, skipping the node to delete"""
            prevNode.set_next(postNode)
            self._size -= 1

        return node

    
    def search(self, element: T) -> int: 
        """returns the index of an element if found else return -1"""
        tempNode = self._head
        index = 0
        while tempNode != None:
            if tempNode.get_data() == element:
                return index
            index += 1
            tempNode = tempNode.get_next()
        return -1

    def getHead(self) -> T:
        """return the head of the SLL or None if empty"""
        return self._head

    def getTail(self) -> T:
        """"returns the tail of the sll or None if empty"""
        return self._tail

    def isEmpty(self) -> bool:
        """returns true if sll is empty."""
        return self._head == None
        # return self._size == 0

    def __str__(self) -> str:
        """ print all the elements of the linked list """
        sll = ""
        tempNode = self._head
        while tempNode:
            sll += f"{tempNode.get_data()} -> "
            # print(f"{tempNode.get_data()}", end=" -> ")
            tempNode = tempNode._next 
        # print("None")
        sll += "None"
        return sll
    
    def clear(self):
        """removes all element from the list"""
        self._head, self._tail = None, None

    def size(self) -> int:
        return self._size

# tests: only runs in the current module but ignored if imported into another module
if __name__ == "__main__": 

    """sll that stores strings """
    print("initial sll:")
    sll_str = SinglyLinkedList[str]()
    print(f"initial size: {sll_str.size()}") # returns 0
    print(f"is sll empty? {sll_str.isEmpty()}") # prints True or False
    print(f"head node: {sll_str.getHead()}")
    print(f"tail node: {sll_str.getTail()}")

    # add elements to the beginning
    print("\nadd elements to the begining of the sll")
    sll_str.add_first("prince") # add str to sll as the head
    print(f"SLL content: {sll_str}")
    print(f"size of sll: {sll_str.size()}")
    print(f"head node: {sll_str.getHead()}")
    print(f"tail node: {sll_str.getTail()}")
    sll_str.add_first("adom") # adds str to sll as the head
    print(f"SLL content: {sll_str}")
    print(f"size of sll: {sll_str.size()}")
    print(f"head node: {sll_str.getHead()}")
    print(f"tail node: {sll_str.getTail()}")
    sll_str.add_first("kofi")
    print(f"size of sll: {sll_str.size()}")

    
    print(f"SLL content: {sll_str}")
    print(f"size of sll: {sll_str.size()}") 
    print(f"head node: {sll_str.getHead()}")
    print(f"tail node: {sll_str.getTail()}")

    # add elements to the end of the sll
    print("\nadd elements to the end")
    sll_str.add_last("kotomi") # add str to sll as the head
    print(f"SLL content: {sll_str}")
    print(f"size of sll: {sll_str.size()}")
    print(f"head node: {sll_str.getHead()}")
    print(f"tail node: {sll_str.getTail()}")
    sll_str.add_last("baiZhetai") # adds str to sll as the head
    print(f"SLL content: {sll_str}")
    print(f"size of sll: {sll_str.size()}")
    print(f"head node: {sll_str.getHead()}")
    print(f"tail node: {sll_str.getTail()}")
    sll_str.add_last("droplet")
    print(f"size of sll: {sll_str.size()}")
    print(f"SLL content: {sll_str}")
    print(f"size of sll: {sll_str.size()}")
    print(f"head node: {sll_str.getHead()}")
    print(f"tail node: {sll_str.getTail()}")

    # searching for an element in the sll
    query = "kofi"
    index = sll_str.search(query)
    found = index != -1
    if found:
        print(f"\"{query}\" found at index {index}")
    else:
        print()
    
    print(f"current size: {sll_str.size()}") # returns 0

    print(sll_str.removeHead())
    print(f"SLL content: {sll_str}") 
    print(sll_str.size())
    sll_str.removeTail()
    print(f"SLL content: {sll_str}")
    print(sll_str.size())

    # remove element from somewhere other than the head or tail
    sll_str.removeElement("prince")
    print(f"SLL content: {sll_str}")
    print(sll_str.size())
