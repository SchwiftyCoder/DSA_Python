from typing import TypeVar, Optional, Generic

T = TypeVar("T")


class TreeNode(Generic[T]):

    def __init__(self, data: T, parent=None) -> None:
        """
        Argument:
            data: the value being stored at the node
            parent: parent of the current node. if root, this value is None. default value is also None

            a node may contain an arbitrary number of nodes, thus the use of list
            We can also set a limit on the number of child node a particular node can store

        """
        self._data = data
        self._children = []
        self._parent = parent

    def add_child(self, child_node: Optional[T]) -> None:
        """
        Argument:
            child_node: the node to add to the tree of generic type T

            Algo:
            add a
        """
        # set the parent of the child node to self, i.e. the current instance of the object
        child_node.parent = self
        self._children.append(child_node)

    def remove_child(self, child_node) -> None:
        """
            builds a new list of children by adding all children except the one to remove
            O(n) complexity
            only removes child one level down
        """
        self._children = [child for child in self._children if child is not child_node]  

    def __repr__(self):
        """ for develoers only: shows how the object is created. must use repr()  in the print arguments"""
        pass

    def __str__(self):
        """ returns a strig representation of the tree: for end users only. acts as a wrapper around print_tree()"""
        return self.print_tree()

    def print_tree(self, level: int = 0) -> str:
        """
        Argument:
            level: the heirarchy of the tree, default is 0 for root, then 1 for 1st level, 2 for 2nd level, etc
        
        Return: 
            a string representation of the object: root and its children recursively"""  

        # print the root node data first, with indentation level 0
        object_str = ("    " * level) + self._data + "\n"

        # recursively traverse the children of root
        # the base case her eis also implicit: it stops when there are no more children within a node
        for child in self._children:  
            object_str += child.print_tree(level + 1) 

        # at this point, the for loop ends since there are no more children within the the current child node
        return object_str 

    def search_tree(self, query_node, level = 0):
        """
        Algo:
            recursively searches the entire tree to remove a node 


        Returns:
            the node being removed as well as the level where it was found

        """   
        pass

    def root(self):
        """
        
        Return:
            the root element of the tree
        """
        pass

    def get_parent(self, child_node):
        """
        Argument:
            child node whose parent we want
        
        Return: 
            get the parent node of the child node
        """
        raise NotImplementedError("Implement me")

    def num_children(self):
        """
        Return:
            the number of children in the tree
        """
        pass

 

if __name__ == "__main__":

    root = TreeNode[str]("vehicle")

    honda = TreeNode[str]("Honda")
    honda.add_child(TreeNode[str]("Civic"))
    honda.add_child(TreeNode[str]("Accord"))
    honda.add_child(TreeNode[str]("CRV"))

    toyota = TreeNode[str]("Toyota")
    toyota.add_child(TreeNode[str]("Camry"))
    toyota.add_child(TreeNode[str]("Avalone"))
    toyota.add_child(TreeNode[str]("Crown"))

    nissan = TreeNode[str]("Nissan")
    nissan.add_child(TreeNode[str]("Rogue"))
    nissan.add_child(TreeNode[str]("360z"))
    nissan.add_child(TreeNode[str]("nissancar"))

    root.add_child(honda)
    root.add_child(toyota)
    root.add_child(nissan)


    print(root)

    # remove a node
    root.remove_child(nissan)

    print(root)
