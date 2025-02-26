# https://leetcode.com/problems/copy-list-with-random-pointer/description/

from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        oldToCopy = {}

        cur = head
        while cur:

            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head

        while cur:
            copied = oldToCopy.get(cur)

            copied.next = oldToCopy.get(cur.next)
            copied.random = oldToCopy.get(cur.random)
            cur = cur.next

        return oldToCopy[head]
