"""
Dijkstra's Algorithm (Python)

Finds the shortest path from a source node to all other nodes in a weighted graph with non-negative edge weights.

Algorithm:
- Uses a min-heap (priority queue) to always expand the node with the smallest known distance.
- Updates distances to neighbors if a shorter path is found.
- Works for both connected and disconnected graphs (unreachable nodes will have distance = inf).

Graph Representation:
- Adjacency list: {node: [(neighbor, weight), ...], ...}

Usage:
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    print(dijkstra(graph, 0))  # {0: 0, 1: 3, 2: 1, 3: 4}

"""

import heapq


def dijkstra(graph, source):
    """
    Computes shortest distances from source to all other nodes using Dijkstra's algorithm.

    Args:
        graph: dict[int, list[tuple[int, int]]] - adjacency list, weights must be non-negative
        source: int - starting node

    Returns:
        dict[int, float] - shortest distances from source to each node
    """
    # Initialize distances
    dist = {node: float("inf") for node in graph}
    dist[source] = 0

    # Min-heap: (distance, node)
    heap = [(0, source)]

    while heap:
        curr_dist, u = heapq.heappop(heap)
        # If we already found a better path, skip
        if curr_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))
    return dist


if __name__ == "__main__":
    # Example 1: Simple graph
    graph1 = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
    print("Shortest distances from 0:", dijkstra(graph1, 0))  # {0: 0, 1: 3, 2: 1, 3: 4}

    # Example 2: Disconnected graph
    graph2 = {0: [(1, 2)], 1: [(2, 3)], 2: [], 3: [(4, 1)], 4: []}
    print(
        "Shortest distances from 0:", dijkstra(graph2, 0)
    )  # {0: 0, 1: 2, 2: 5, 3: inf, 4: inf}

    # Example 3: Single node
    graph3 = {0: []}
    print("Shortest distances from 0:", dijkstra(graph3, 0))  # {0: 0}

    # Example 4: Negative weights (should not be used with Dijkstra's)
    graph4 = {0: [(1, -1)], 1: [(2, 2)], 2: []}
    print(
        "Shortest distances from 0 (negative weights):", dijkstra(graph4, 0)
    )  # {0: 0, 1: -1, 2: 1}
    print(
        "WARNING: Dijkstra's algorithm does not work correctly with negative weights!"
    )
