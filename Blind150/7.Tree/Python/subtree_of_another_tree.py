# https://leetcode.com/problems/subtree-of-another-tree/description/
# Definition for a binary tree node.

import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same_tree(p, q):

            if not p and not q:
                return True

            if not all([p,q]):
                return False

            if p.val != q.val:
                return False

            if not is_same_tree(p.left, q.left) or not is_same_tree(p.right, q.right):
                return False

            return True

        dq = collections.deque([root])
        possible_roots = []

        while dq:

            cur = dq.popleft()

            if cur.val == subRoot.val:
                possible_roots.append(cur)

            if cur.left:
                dq.append(cur.left)

            if cur.right:
                dq.append(cur.right)

        """
        possible_roots is populated from left to right in level-order (BFS).
        This means nodes at lower depths (closer to the root) appear earlier in the list.
        When you iterate normally (possible_roots), you are checking from shallower nodes to deeper nodes.
        When you iterate in reverse order (possible_roots[::-1]), you are checking deeper nodes first.

        If a deeper node is the correct subtree, checking it first means fewer calls to is_same_tree(),
        which reduces the number of unnecessary recursive calls.

        In cases where subRoot is deep inside root, this approach finds a match sooner, leading to better performance.
        """

        for r in possible_roots[::-1]:
            if is_same_tree(r, subRoot):
                return True

        return False
