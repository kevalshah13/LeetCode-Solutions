class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        from collections import defaultdict
        adjlist=defaultdict(list)
        for i in edges:
            adjlist[i[0]].append(i[1])
            adjlist[i[1]].append(i[0])
        visited=[0 for i in range(n)]
        def DFS(source):
            visited[source]=1
            for i in adjlist[source]:
                if visited[i]==0:
                    visited[i]=1
                    DFS(i)
        DFS(source)
        return visited[destination]