# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        s,f = head, head.next

        while f and f.next:

            s = s.next
            f = f.next.next


        snd = s.next

        s.next = None

        # reverse the 2nd half

        prev = None

        while snd:

            tmp = snd.next
            snd.next = prev
            prev = snd
            snd = tmp


        # merge both the lists
        # snd = prev ; because , after the previous loop is done snd will be
        # none and prev will the head of the snd half of the List

        ft, sd = head, prev

        while sd:

            tmp1, tmp2 = ft.next, sd.next

            ft.next = sd
            sd.next = tmp1
            ft,sd = tmp1, tmp2
