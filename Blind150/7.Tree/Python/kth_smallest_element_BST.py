# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        elms = []

        def inorder(root):

            nonlocal elms

            if not root:
                return

            inorder(root.left)

            if len(elms) == k:
                return

            elms.append(root.val)

            inorder(root.right)

        inorder(root)

        return elms[-1]
