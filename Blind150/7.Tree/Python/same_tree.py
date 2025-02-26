# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not all([p,q]):
            return False

        if p.val != q.val:
            return False

        if not self.isSameTree(p.left, q.left) or not self.isSameTree(p.right, q.right):
            return False

        return True
