"""

100. Same Tree
Easy 
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""

from typing import Optional
from treenode import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach:
            1. perform a DFS preOrder traversal on both trees simultaneoulsy
            2. a. if both nodes are none, return true
               b. if only one node is none, return False
               c. if the values being heling held are not the same, return False
            3. recursively check the left and right subtrees
        """
        # both are none
        if not p and not q:
            return True
        
        # only one is none
        if not p or not q:
            return False
        
        # both are not none but value is different
        if p.val != q.val:
            return False

        # recursively check the left and right subtrees
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        
        # if both left and right subtrees are the same, return True
        return left_same and right_same


# build a binary tree with some values
if __name__ == "__main__":
    root_1 = TreeNode(1)
    root_1.left = TreeNode(2)
    root_1.right = TreeNode(3)

    root_2 = TreeNode(1)
    root_2.left = TreeNode(2)
    root_2.right = TreeNode(3)

    sol = Solution()

    # example 1: true
    if sol.isSameTree(root_1, root_2):
        print(f"Trees are the same") # prit this out
    else:
        print(f"Trees are different")

    # example 2: false
    root_a = TreeNode(1)
    root_b = TreeNode(1)

    root_a.left = TreeNode(2)
    root_b.right = TreeNode(2)

    if sol.isSameTree(root_a, root_b):
        print(f"Trees are the same") # prit this out
    else:
        print(f"Trees are different")

