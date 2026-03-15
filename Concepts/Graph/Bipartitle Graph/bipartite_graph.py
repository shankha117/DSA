"""
Bipartite Graph Checker (Python)

A graph is bipartite if its vertices can be divided into two disjoint sets such that every edge connects a vertex from one set to a vertex from the other set. Equivalently, a graph is bipartite if it is possible to color its vertices with two colors such that no two adjacent vertices share the same color.

This implementation uses BFS to check bipartiteness by coloring the graph.

Usage:
    - The graph is represented as an adjacency list: a dictionary mapping each node to a list of its neighbors.
    - Call is_bipartite(graph) to check if the graph is bipartite.

Example:
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }
    print(is_bipartite(graph))  # True

    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    print(is_bipartite(graph))  # False (odd cycle)
"""

from collections import deque


def is_bipartite(graph):
    """
    Checks if the given undirected graph is bipartite using BFS coloring.

    Args:
        graph: dict[int, list[int]] - adjacency list representation

    Returns:
        True if the graph is bipartite, False otherwise.
    """
    color = {}
    for node in graph:
        if node not in color:
            queue = deque()
            queue.append(node)
            color[node] = 0  # Assign first color
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True


if __name__ == "__main__":
    # Test cases
    bipartite_graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
    print("Bipartite (should be True):", is_bipartite(bipartite_graph))

    non_bipartite_graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    print("Not Bipartite (should be False):", is_bipartite(non_bipartite_graph))

    # Disconnected graph with bipartite and non-bipartite components
    mixed_graph = {0: [1], 1: [0], 2: [3, 4], 3: [2, 4], 4: [2, 3]}
    print("Mixed (should be False):", is_bipartite(mixed_graph))
