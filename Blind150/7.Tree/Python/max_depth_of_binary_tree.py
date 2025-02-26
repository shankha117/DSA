# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        leftDepth = 1 + self.maxDepth(root.left)
        RightDepth = 1 + self.maxDepth(root.right)

        return max(leftDepth, RightDepth)
