// https://leetcode.com/problems/merge-k-sorted-lists/description/
package main

import (
	"container/heap"
)

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Item holds the value and reference to the current node and list index
type Item struct {
	val  int
	idx  int
	node *ListNode
}

// PriorityQueue implements heap.Interface
type PriorityQueue []Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].val < pq[j].val
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x any) {
	*pq = append(*pq, x.(Item))
}

func (pq *PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[:n-1]
	return item
}

// mergeKLists merges k sorted linked lists
func mergeKLists(lists []*ListNode) *ListNode {
	pq := &PriorityQueue{}
	heap.Init(pq)

	for idx, node := range lists {
		if node != nil {
			heap.Push(pq, Item{val: node.Val, idx: idx, node: node})
		}
	}

	dummy := &ListNode{}
	current := dummy

	for pq.Len() > 0 {
		item := heap.Pop(pq).(Item)
		current.Next = &ListNode{Val: item.val}
		current = current.Next
		if item.node.Next != nil {
			heap.Push(pq, Item{val: item.node.Next.Val, idx: item.idx, node: item.node.Next})
		}
	}

	return dummy.Next
}
