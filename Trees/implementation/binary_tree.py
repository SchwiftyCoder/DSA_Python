from typing import TypeVar, Optional, Generic
from numbers import Number
from treenode import TreeNode
from queue import Queue

# N represents a generic type restructed to only numerical values
N = TypeVar("N", bound=Number)

class BinaryTree(Generic[N]):
    """ this class works exclusively wiht numbers """

    def __init__(self) -> None: 
        """ initializes a binary tree with root, left and right nodes being None"""
        self._root: Optional['TreeNode[N]'] = None 

    def insert(self, data: N) -> None:
        """
        validates that the data to insert is a number
        inserts a value into the binary tree
        if root of tree is empty, then insert into tree otherwise insert into children

        Args:
            data: the integer value to insert into the tree 

        Default Order: 
            level: from left to right

        Return:
            None
        """
        data = self.validate_object(data)
        node_to_add = TreeNode(data)

        if self._root is None:
            self._root = node_to_add
        else: 
            node_queue = Queue()
            node_queue.put(self.get_root())
            while node_queue:
                curr = node_queue.get() 
                if curr.get_left():
                    node_queue.put(curr.get_left())
                else:
                    curr.set_left(node_to_add)
                    break
                if curr.get_right():
                    node_queue.put(curr.get_right())
                else:
                    curr.set_right(node_to_add)
                    break

    @staticmethod
    def validate_object(number: N) -> N:
        """ validates that the provided object is a number """
        # print(f"Validating: {number}")  # Debug print to confirm method invocation
        if not isinstance(number, Number):
            raise ValueError("Binary Tree works exclusively wth numbers")
        return number
    
    # depth-first traversals 
    def in_order_traversal(self) -> Optional[str]:
        return self.in_order_traversal(self.get_root())
    
    def in_order_traversal(self, node: Optional["TreeNode[N]"]) -> str:
        """
        order: left > root > right
        """

        # base case
        if node is None:
            return ""

        # recursive case
        left_child = self.in_order_traversal(node.get_left())
        right_child = self.in_order_traversal(node.get_right())

        return left_child + str(node) + right_child

    def post_order_traversal(self) -> Optional[str]:
        """
        order: left > right > root
        """
        pass

    def pre_order_traversal(self) -> Optional[str]:
        """ 
        order: root > left > right
        """
        pass 

    # breadth first traversal
    def level_order_traversal(self) -> Optional[str]:
        """
        order: start at root, and then left to right
        A node and its children are stored in a queue. 

        Return: 
            A string representation of the nodes, starting from root
        """
        tree_content = "["
        if self.get_root() is None:
            return "[]"
        node_queue = Queue()
        node_queue.put(self.get_root())

        while not node_queue.empty():
            curr = node_queue.get()
            tree_content += str(curr) + ", "
            if curr.get_left():
                node_queue.put(curr.get_left())
            if curr.get_right():
                node_queue.put(curr.get_right())

        return tree_content + "]"

    def delete(self, node: N) -> Optional['BinaryTree[Number]']:
        """
        Cases:
         * deletion requires handling three cases: 
         * a leaf node, simply set to None
         * a node with one child, and 
         * a node with two children.

        Argument:
            node: the node to delete

        Return:
            the deleted node
        """
        pass

    def search(self, node: N) -> bool:
        """
        Return:
            True if a value exists within the tree else False

            Uses a level order traversal
        """
        pass

    def find_max(self) -> Optional['BinaryTree[N]']:
        """
        Return:
            the max number in the binary tree
        """
        pass

    def find_min(self) -> Optional['BinaryTree[N]']:
        """
        Return:
            the min number in the binary tree
        """ 
        pass

    def height(self) -> int:
        """
        Return:
            height of the tree, which is the number of edges on the longest path from the root to a leaf. 
        """

    def get_root(self) -> Optional['TreeNode[N]']: 
        return self._root


if __name__ == "__main__":
    tree = BinaryTree[int]()
    tree.insert(90) 
    tree.insert(-1)
    tree.insert(34)
    tree.insert(12)

    print(f"root node of tree: {tree.get_root()}")
    print(f"Level order traversal of tree: {tree.level_order_traversal()}")
    print(f"in orde rtraversal of the tree: {tree.in_order_traversal()}")

