# You are given an undirected graph with n nodes labeled from 0 to n-1 and a list of edges.
# Each edge connects two different nodes.
# Return True if the graph contains a cycle, otherwise return False.


# n = 5
# edges = [
#     [0, 1],
#     [1, 2],
#     [2, 3],
#     [1, 3]
# ]


class Solution:
    def hasCycle(self, n: int, edges: list[list[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            # Path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            # Cycle detected
            if root_x == root_y:
                return False

            # Union by rank
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return True

        return False
