# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def find_diameter(root):
            nonlocal res
            if not root:
                return 0

            d_l = find_diameter(root.left)
            d_r = find_diameter(root.right)

            d = d_l + d_r

            res = max(res, d)

            return 1+ max(d_l, d_r)

        find_diameter(root)

        return res
