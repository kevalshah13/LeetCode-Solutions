class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, node, parent, adj):
        for neighbor, sign in adj[node]:
            if neighbor != parent:
                self.count += sign  # Add to count if road needs reordering
                self.dfs(neighbor, node, adj)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append((v, 1))  # Road from u to v needs reordering
            adj[v].append((u, 0))  # Road from v to u doesn't need reordering

        self.dfs(0, -1, adj)  # Start DFS from node 0 with no parent (-1)
        return self.count