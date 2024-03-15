from typing import TypeVar, Generic, Optional
N = TypeVar("N")


class TreeNode(Generic[N]):
    def __init__(self, data: N) -> None:
        """
        Initialize a new TreeNode with the given data.

        Args:
            data: The data to store in the node. Can be of any type N.
        """
        self._data = data
        self._left: Optional['TreeNode[N]'] = None
        self._right: Optional['TreeNode[N]'] = None

    def set_left(self, data: N) -> None:
        """
        Create a new TreeNode with the given data and set it as the left child of this node.

        Args:
            data: The data to store in the left child node.
        """
        self._left = TreeNode(data)

    def set_right(self, data: N) -> None:
        """
        Create a new TreeNode with the given data and set it as the right child of this node.

        Args:
            data: The data to store in the right child node.
        """
        self._right = TreeNode(data)

    def get_left(self) -> Optional['TreeNode[N]']:
        """
        Return the left child of this node, if it exists.

        Returns:
            The left child TreeNode if it exists, otherwise None.
        """
        return self._left

    def get_right(self) -> Optional['TreeNode[N]']:
        """
        Return the right child of this node, if it exists.

        Returns:
            The right child TreeNode if it exists, otherwise None.
        """
        return self._right

    def is_leaf(self) -> bool:
        """
        Check if this node is a leaf node.

        A leaf node has no children.

        Returns:
            True if this node is a leaf node, False otherwise.
        """
        # criteria: check both left and right children are None
        return self._left is None and self._right is None

    def remove_child(self, child: 'TreeNode[N]') -> bool:
        """
        Remove a child node from this node.

        If the specified child node matches one of this node's children,
        that child is removed.

        Args:
            child: The child TreeNode to remove.

        Returns:
            bool: True if the child was found and removed, False otherwise.
        """
        if self._left._data == child._data:
            # self._left = None
            self.set_left(None)
            return True
        elif self._right._data == child._data:
            # self._right = None
            self.set_right(None) # better encapsulation
            return True
        else:
            return False # child node to remove is not found at the current/this node
            

    def has_left_child(self) -> bool:
        """
        Check if this node has a left child.

        Returns:
            True if this node has a left child, False otherwise.
        """
        return self.get_left() is not None

    def has_right_child(self) -> bool:
        """
        Check if this node has a right child.

        Returns:
            True if this node has a right child, False otherwise.
        """
        return self.get_right() is not None

    def get_children_count(self) -> int:
        """
        Args:
            node: the node to find the number of its children

        Returns:
            The number of children (0, 1, or 2) of this node.
        """
        # assume the node itself is not None
        if self.get_left() is None and self.get_right() is None:
            return 0
        elif self.get_left() and self.get_right():
            return 2
        else:
            return 1

        
    
    def get_children_and_descendants_count(node: 'TreeNode[N]') -> int:
        """
        recursively counts the direct children and all descendants of a given node
        
        Args:
            node: the node to find the number of its children

        Returns:
            all the children and descendants of this node.
        """
        
        # helper method to recursively count the number of left and right childs of the current node
        def count_children(node: 'TreeNode[N]'):
            # base case: node has no children
            if node is None:
                return 0
            # recursive case, +1 is the count of the current node being processed, not its .left/.right
            # +1 to the previous recursive calls eventually tallies up to the number of nodes
            # the + between .left and .right si to ensure that we add the count of all left and then right  # sub trees and then return the ovrall sum
            return count_children(node.get_left()) + count_children(node.get_right()) + 1
                
        # -1 is a correction to exclude the head from the count
        return count_children(node) - 1
    
    def __str__(self) -> str:
        return str(self._data)
    


# perform tests
    
if __name__ == "__main__":
    root = TreeNode[int](34)
    root.set_left(1) 
    root.set_right(31)
    root.get_left().set_right(12)

    print(root.has_right_child())

    print(root.get_children_count())
    print()

    print(root.get_children_and_descendants_count())

    print(root.get_left().get_right())
