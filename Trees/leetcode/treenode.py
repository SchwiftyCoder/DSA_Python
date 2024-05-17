from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Optional["TreeNode"] = left
        self.right: Optional["TreeNode"] = right
