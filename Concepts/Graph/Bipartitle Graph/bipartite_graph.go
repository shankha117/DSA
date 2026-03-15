package main

import (
	"fmt"
)

// isBipartite checks if the given undirected graph is bipartite.
// The graph is represented as an adjacency list: graph[i] contains all nodes adjacent to node i.
// Returns true if the graph is bipartite, false otherwise.
//
// Approach:
// - Use BFS to try to color the graph with two colors (0 and 1).
// - If any adjacent nodes have the same color, the graph is not bipartite.
// - Handle disconnected graphs by running BFS from every unvisited node.
func isBipartite(graph [][]int) bool {
	n := len(graph)
	color := make([]int, n)
	for i := range color {
		color[i] = -1 // -1 means uncolored
	}

	for start := 0; start < n; start++ {
		if color[start] != -1 {
			continue // already colored
		}
		queue := []int{start}
		color[start] = 0
		for len(queue) > 0 {
			node := queue[0]
			queue = queue[1:]
			for _, neighbor := range graph[node] {
				if color[neighbor] == -1 {
					color[neighbor] = 1 - color[node]
					queue = append(queue, neighbor)
				} else if color[neighbor] == color[node] {
					return false
				}
			}
		}
	}
	return true
}

func main() {
	// Example 1: Bipartite graph
	// 0---1
	// |   |
	// 3---2
	graph1 := [][]int{
		{1, 3},
		{0, 2},
		{1, 3},
		{0, 2},
	}
	fmt.Printf("Graph1 is bipartite? %v\n", isBipartite(graph1)) // true

	// Example 2: Not bipartite (odd cycle)
	// 0---1
	//  \  /
	//   2
	graph2 := [][]int{
		{1, 2},
		{0, 2},
		{0, 1},
	}
	fmt.Printf("Graph2 is bipartite? %v\n", isBipartite(graph2)) // false

	// Example 3: Disconnected graph, both components bipartite
	graph3 := [][]int{
		{1},    // 0
		{0},    // 1
		{3, 4}, // 2
		{2, 4}, // 3
		{2, 3}, // 4
	}
	fmt.Printf("Graph3 is bipartite? %v\n", isBipartite(graph3)) // true

	// Example 4: Empty graph
	graph4 := [][]int{}
	fmt.Printf("Graph4 is bipartite? %v\n", isBipartite(graph4)) // true

	// Example 5: Single node
	graph5 := [][]int{{}}
	fmt.Printf("Graph5 is bipartite? %v\n", isBipartite(graph5)) // true
}
