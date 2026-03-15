# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Definition for singly-linked list.
from typing import Optional, List
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        head = tmp = ListNode()

        if not lists:
            return head.next

        for idx, node  in enumerate(lists):

            if node:
                heap.append((node.val, idx, node.next))


        heapq.heapify(heap)

        while heap:

            cur_val , idx, next_node = heapq.heappop(heap)

            tmp.next = ListNode(cur_val)
            tmp = tmp.next

            # add the next node

            if next_node:
                heapq.heappush(heap, (next_node.val, idx, next_node.next))


        return head.next
