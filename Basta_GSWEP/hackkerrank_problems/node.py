from typing import Any, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data  # holds the value assigned to the node
        self.next: Optional["Node"] = (
            None  # pointer to the next node in the list, can be None
        )


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None  # starting point of the list (initially empty)

    def append(self, data: Any) -> None:
        """Append a node with the given data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If the list is empty, the new node becomes the head
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link the last node to the new node

    def display(self) -> None:
        """Display all the nodes in the list."""
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()  # Newline for clean output

    def to_list(self) -> list:
        """Convert linked list to Python list (mostly for testing)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    # @property
    def head(self) -> Optional[Node]:
        return self.head
