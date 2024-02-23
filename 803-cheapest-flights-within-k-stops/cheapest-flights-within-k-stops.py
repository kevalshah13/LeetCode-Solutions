class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = [[] for _ in range(n)]
    minHeap = [(0, src, k + 1)]  # (d, u, stops)
    dist = [[math.inf] * (k + 2) for _ in range(n)]

    for u, v, w in flights:
      graph[u].append((v, w))

    while minHeap:
      d, u, stops = heapq.heappop(minHeap)
      if u == dst:
        return d
      if stops > 0:
        for v, w in graph[u]:
          newDist = d + w
          if newDist < dist[v][stops - 1]:
            dist[v][stops - 1] = newDist
            heapq.heappush(minHeap, (newDist, v, stops - 1))

    return -1



# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         adj=defaultdict(list)
#         for i in flights:
#             adj[i[0]].append((i[1],i[2]))
#         print(adj)
#         dist=[math.inf for i in range(n)]
#         q=[src]
#         c=0
#         while q:
#             j=q[0]
#             for m in adj[j]:
#                 q.append(m[0])
#                 if c>=k:
#                     break
#                 dist[m[0]]=min(dist[m[0]],dist[j]+m[1])
#             c+=1
#             del q[0]
#         print(dist)
#         return dist[dst]
