# class Solution:
#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
#         A=defaultdict(set)
#         B=defaultdict(set)
#         # C=defaultdict(list)
#         for i in edges:
#             if i[0]==1 or i[0]==3:
#                 A[i[1]].add(i[2])
#                 A[i[2]].add(i[1])
#             if i[0]==2 or i[0]==3:
#                 B[i[1]].add(i[2])
#                 B[i[2]].add(i[1])
#         print(A)
#         print(B)
#         return 0
class Solution:

    def check_conectivity(self, n, edges_1, edges_2):
        visited = (n + 1) * [False]

        stack = [1]

        while stack:
            curr = stack.pop()
            if visited[curr]:
                continue
            visited[curr] = True
            stack.extend(edges_1[curr])
            stack.extend(edges_2[curr])

        return sum(visited) == n

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        type_1_neighbors = [[] for i in range(n + 1)]
        type_2_neighbors = [[] for i in range(n + 1)]
        type_3_neighbors = [[] for i in range(n + 1)]

        for t, u, v in edges:
            if t == 1:
                type_1_neighbors[u].append(v)
                type_1_neighbors[v].append(u)
            elif t == 2:
                type_2_neighbors[u].append(v)
                type_2_neighbors[v].append(u)
            else:
                type_3_neighbors[u].append(v)
                type_3_neighbors[v].append(u)

        
        if not self.check_conectivity(n, type_1_neighbors, type_3_neighbors) or not self.check_conectivity(n, type_2_neighbors, type_3_neighbors):
            return -1

        visited = (n + 1) * [False]

        components = 0
        for i in range(1, n + 1):
            if visited[i]:
                continue
            
            components += 1
            stack = [i]

            while stack:
                curr = stack.pop()

                if visited[curr]:
                    continue
                
                visited[curr] = True

                stack.extend(type_3_neighbors[curr])


        spanning_edges = n - components

        # add edges to get connectivity for alice and bob
        if spanning_edges < n - 1:
            spanning_edges += 2* (n - 1 -  spanning_edges)
        
        return len(edges) - spanning_edges
