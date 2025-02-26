# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description

from typing import List,Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        # root_pos_inorder = 0

        # for pos, val in enumerate(inorder):

        #     if val == root.val:

        #         root_pos_inorder = pos

        root_pos_inorder = inorder.index(root.val)

        inorder_left, inorder_right = inorder[:root_pos_inorder], inorder[root_pos_inorder+1:]

        preorder_left, preorder_right =  preorder[1:len(inorder_left)+1], preorder[len(inorder_left)+1:]


        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
