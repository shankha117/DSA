# Bipartite Graph: Problem Statement & Algorithm Explanation

## Problem Statement

A graph is called **bipartite** if its vertices can be divided into two disjoint sets such that every edge connects a vertex from one set to a vertex from the other set. In other words, no two vertices within the same set are adjacent.

**Given:**  
- An undirected graph (can be represented as an adjacency list or adjacency matrix).

**Task:**  
- Determine whether the graph is bipartite.

---

## Intuition

A bipartite graph can be "colored" using two colors such that no two adjacent vertices share the same color. If such a coloring is possible, the graph is bipartite.

This property is equivalent to saying the graph contains **no odd-length cycles**.

---

## Algorithm (BFS/DFS Coloring)

### Approach

1. **Coloring:**  
   - Assign colors (say, 0 and 1) to each vertex such that no two adjacent vertices have the same color.
   - If at any point you find two adjacent vertices with the same color, the graph is not bipartite.

2. **Traversal:**  
   - Use either BFS or DFS to traverse the graph and assign colors.
   - Since the graph may be disconnected, repeat the process for each connected component.

### Steps

#### BFS Version

1. Initialize a color array (or map) with -1 (uncolored) for all vertices.
2. For each uncolored vertex, start a BFS:
   - Assign color 0 to the starting vertex.
   - For each neighbor:
     - If uncolored, assign the opposite color and add to the queue.
     - If already colored and the color matches the current vertex, return False (not bipartite).
3. If all vertices are colored without conflict, return True (bipartite).

#### DFS Version

1. Similar to BFS, but use recursion to assign colors.
2. For each uncolored vertex, start DFS:
   - Assign a color.
   - For each neighbor:
     - If uncolored, recursively assign the opposite color.
     - If already colored and the color matches the current vertex, return False.
3. If all vertices are colored without conflict, return True.

---

## Example

Consider the following graph (adjacency list):

```
0: [1, 3]
1: [0, 2]
2: [1, 3]
3: [0, 2]
```

- This graph is bipartite:  
  - Set A: {0, 2}  
  - Set B: {1, 3}

Now consider a triangle:

```
0: [1, 2]
1: [0, 2]
2: [0, 1]
```

- This graph is **not** bipartite (it contains an odd-length cycle).

---

## Complexity

- **Time:** O(V + E), where V is the number of vertices and E is the number of edges.
- **Space:** O(V) for the color array and traversal queue/stack.

---

## Summary

- Bipartite graphs can be colored with two colors such that no two adjacent vertices share the same color.
- Use BFS or DFS to attempt coloring.
- If a coloring conflict is found, the graph is not bipartite.
- Works for both connected and disconnected graphs.

---