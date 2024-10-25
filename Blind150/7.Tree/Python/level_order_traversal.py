# https://leetcode.com/problems/binary-tree-level-order-traversal/description/


from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        d = deque([root])

        ans = []

        while d:

            level_list = []

            for _ in range(len(d)):
                n = d.popleft()
                level_list.append(n.val)

                if n.left:
                    d.append(n.left)

                if n.right:
                    d.append(n.right)

            ans.append(level_list)

        return ans
