# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        add = ListNode()

        ans = add


        carry = 0

        while l1 and l2:

            a,b = l1.val, l2.val

            carry , value = divmod(a+b+carry,10)

            add.next = ListNode(value)

            l1 ,l2,add = l1.next, l2.next, add.next

        while l1:

            carry , value = divmod(l1.val+carry,10)

            add.next = ListNode(value)

            l1,add = l1.next,add.next

        while l2:

            carry , value = divmod(l2.val+carry,10)

            add.next = ListNode(value)

            l2,add = l2.next, add.next

        if carry:

            add.next = ListNode(carry)

        return ans.next
