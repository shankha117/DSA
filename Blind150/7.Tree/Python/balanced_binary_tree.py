# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isunbalanced = False

        def is_balanced(root):
            nonlocal isunbalanced
            if not root or isunbalanced:
                return 0  # Return 0 for null nodes or stop further calculations if already unbalanced

            left_height = is_balanced(root.left)
            right_height = is_balanced(root.right)

            # Check if the current node is balanced
            if abs(left_height - right_height) > 1:
                isunbalanced = True

            return 1 + max(
                left_height, right_height
            )  # Return the height of the current subtree

        is_balanced(root)

        return not isunbalanced
