# Check Obsidian ALSO

> **Detecting cycles in an undirected graph using Union-Find**

You can directly copy-paste this into a `.md` file (GitHub / Obsidian / Notion / docs).

---

````md
# Cycle Detection in an Undirected Graph using Union-Find (Disjoint Set)

Detecting cycles in an undirected graph is a common problem in graph theory and interviews.  
One of the most efficient and elegant ways to solve this is using the **Union-Find (Disjoint Set Union – DSU)** data structure.

---

## Problem Statement

Given an **undirected graph** with `n` vertices and a list of edges, determine whether the graph contains a **cycle**.

---

## Key Idea (Intuition)

- Each connected component of the graph is treated as a **set**
- Initially, every vertex is in its **own set**
- For every edge `(u, v)`:
  - If `u` and `v` already belong to the **same set**, adding this edge creates a **cycle**
  - Otherwise, merge (union) the two sets

This works because, in an undirected graph, a cycle exists **if and only if** we try to connect two vertices that are already connected.

---

## Union-Find (Disjoint Set) Basics

Union-Find supports two operations:

- **find(x)** → Finds the representative (root) of the set containing `x`
- **union(x, y)** → Merges the sets containing `x` and `y`

---

## Basic Union-Find Implementation (Python)

```
class UnionFind:
    def __init__(self, n):
        # Each node is its own parent initially
        self.parent = [i for i in range(n)]

    def find(self, x):
        # Find the root of x
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        # Attach root of y to root of x
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent[root_y] = root_x
````

---

## Cycle Detection Algorithm

### Steps

1. Initialize Union-Find with `n` nodes
2. Iterate through all edges
3. For each edge `(u, v)`:

   * If `find(u) == find(v)` → **cycle detected**
   * Else → `union(u, v)`

---

## Python Code: Cycle Detection in Undirected Graph

```python
def has_cycle(n, edges):
    """
    n     : number of vertices
    edges : list of (u, v) pairs
    """
    uf = UnionFind(n)

    for u, v in edges:
        # If u and v are already in the same set,
        # adding this edge creates a cycle
        if uf.find(u) == uf.find(v):
            return True
        uf.union(u, v)

    return False
```

---

## Example

### Graph

```
0 -- 1
|    |
3 -- 2
```

### Edges

```python
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0)
]
```

### Run

```python
print(has_cycle(4, edges))
```

### Output

```
True
```

✔ A cycle is detected.

---

## Optimized Union-Find (Union by Rank + Path Compression)

To make the algorithm extremely fast, we apply two optimizations:

### 1. Union by Rank

* Always attach the **smaller tree** under the **larger tree**

### 2. Path Compression

* During `find`, make every node point directly to the root

---

## Optimized Union-Find Code

```python
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
```

---

## Cycle Detection Using Optimized Union-Find

```python
def has_cycle(n, edges):
    uf = UnionFind(n)

    for u, v in edges:
        if uf.find(u) == uf.find(v):
            return True
        uf.union(u, v)

    return False
```

---

## Time Complexity

With **union by rank + path compression**:

* Each operation runs in **α(n)** time
* α(n) = inverse Ackermann function (grows extremely slowly)
* Effectively **O(1)** per operation

---

## When to Use Union-Find for Cycle Detection

✅ Undirected graphs
✅ Edge list representation
✅ Dynamic graph connectivity
❌ Directed graphs (DFS is preferred there)

---

## Comparison with DFS

| Method     | Undirected | Directed | Notes                                  |
| ---------- | ---------- | -------- | -------------------------------------- |
| DFS        | ✅          | ✅        | Requires visited + parent tracking     |
| Union-Find | ✅          | ❌        | Faster & simpler for undirected graphs |

---

## Summary

* Union-Find efficiently detects cycles in undirected graphs
* A cycle exists if an edge connects two nodes already in the same set
* Optimizations make it nearly constant time
* Commonly used in **Kruskal’s MST**, **network connectivity**, and **graph validation**

---

## Key Takeaway

> **In an undirected graph, if two vertices of an edge already belong to the same connected component, adding that edge creates a cycle.**

---

Happy coding 🚀

```

---

If you want next:
- 🔹 **Union-Find full notes (all topics) as one MD**
- 🔹 **Interview Q&A section**
- 🔹 **Visual diagrams (ASCII / images)**
- 🔹 **LeetCode problems list using Union-Find**

Just tell me 👍
```
