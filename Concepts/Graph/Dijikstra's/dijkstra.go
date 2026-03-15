package main

import (
	"container/heap"
	"fmt"
	"math"
)

// Dijkstra's algorithm finds the shortest path from a source node to all other nodes in a weighted graph with non-negative edge weights.
// This implementation uses an adjacency list and a min-heap (priority queue).

// Edge represents a connection from one node to another with a given weight.
type Edge struct {
	to     int
	weight int
}

// Graph is represented as an adjacency list: graph[u] contains all edges from node u.
type Graph [][]Edge

// Item is an element in the priority queue.
type Item struct {
	node int
	dist int
}

// PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []Item

func (pq PriorityQueue) Len() int            { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool  { return pq[i].dist < pq[j].dist }
func (pq PriorityQueue) Swap(i, j int)       { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) { *pq = append(*pq, x.(Item)) }
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[:n-1]
	return item
}

// Dijkstra computes shortest distances from source to all nodes.
// Returns a slice of distances (math.MaxInt32 means unreachable).
func Dijkstra(graph Graph, source int) []int {
	n := len(graph)
	dist := make([]int, n)
	for i := range dist {
		dist[i] = math.MaxInt32
	}
	dist[source] = 0

	pq := &PriorityQueue{}
	heap.Init(pq)
	heap.Push(pq, Item{node: source
