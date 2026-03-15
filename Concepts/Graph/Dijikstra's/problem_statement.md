# Dijkstra's Algorithm: Problem Statement & Algorithm Explanation

## Problem Statement

Given a weighted, directed or undirected graph with non-negative edge weights, and a source vertex, find the shortest path from the source to every other vertex in the graph.

**Input:**
- A graph represented as an adjacency list or adjacency matrix.
- Edge weights are non-negative.
- A source vertex.

**Output:**
- The shortest distance from the source to every other vertex.
- (Optionally) The actual shortest paths.

---

## Intuition

Dijkstra's algorithm is a classic greedy algorithm for finding the shortest path from a single source to all other vertices in a graph with non-negative edge weights. It works by iteratively selecting the vertex with the smallest known distance, updating the distances to its neighbors, and repeating until all vertices have been processed.

---

## Algorithm (Priority Queue / Min-Heap Version)

### Approach

1. **Initialization:**
   - Set the distance to the source vertex as 0 and all other vertices as infinity.
   - Use a priority queue (min-heap) to efficiently select the vertex with the smallest tentative distance.

2. **Processing:**
   - While the priority queue is not empty:
     - Extract the vertex `u` with the smallest distance.
     - For each neighbor `v` of `u`:
       - If the path through `u` to `v` is shorter than the current known distance to `v`, update the distance and add `v` to the priority queue.

3. **Termination:**
   - When the priority queue is empty, all shortest distances have been found.

### Steps

1. Initialize a distance array `dist[]` with `dist[source] = 0` and all others as infinity.
2. Initialize a min-heap (priority queue) and insert `(0, source)`.
3. While the queue is not empty:
   - Pop `(current_dist, u)` from the queue.
   - For each neighbor `v` of `u` with edge weight `w`:
     - If `dist[v] > dist[u] + w`, update `dist[v] = dist[u] + w` and push `(dist[v], v)` into the queue.
4. Optionally, maintain a `prev[]` array to reconstruct the shortest paths.

---

## Example

Consider the following graph (adjacency list with weights):

```
0: [(1, 4), (2, 1)]
1: [(3, 1)]
2: [(1, 2), (3, 5)]
3: []
```

Source: 0

- Shortest path from 0 to 1: 0 → 2 → 1 (distance 3)
- Shortest path from 0 to 3: 0 → 2 → 1 → 3 (distance 4)

---

## Complexity

- **Time:** O((V + E) log V) using a min-heap (priority queue), where V is the number of vertices and E is the number of edges.
- **Space:** O(V + E) for the graph representation and auxiliary data structures.

---

## Summary

- Dijkstra's algorithm finds the shortest path from a source to all other vertices in a graph with non-negative edge weights.
- Uses a greedy approach with a priority queue to efficiently select the next vertex to process.
- Works for both directed and undirected graphs.
- Does **not** work correctly with negative edge weights (use Bellman-Ford for those cases).
- Can be extended to reconstruct actual shortest paths using a predecessor array.

---