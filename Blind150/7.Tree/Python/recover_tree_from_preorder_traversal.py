# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        pos = 0

        first_node = ""

        while pos < len(traversal) and traversal[pos] != "-":
            first_node += traversal[pos]
            pos += 1


        stack = [TreeNode(int(first_node))]

        depth = 0

        while pos < len(traversal):

            ch = traversal[pos]

            if ch == "-":
                depth += 1
                pos += 1
            else:
                num = ""
                while pos < len(traversal) and traversal[pos] != "-":
                    num += traversal[pos]
                    pos += 1

                num = int(num)

                new_node = TreeNode(num)

                if stack and len(stack) > depth:
                    while len(stack) > depth:
                        stack.pop()

                    stack[-1].right = new_node
                else:
                    stack[-1].left = new_node

                stack.append(new_node)

                depth = 0

        return stack[0]
