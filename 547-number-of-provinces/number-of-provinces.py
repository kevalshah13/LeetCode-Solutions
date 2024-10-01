from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def BFS(start):
            q=deque([start])
            visited[start]=1
            while(q):
                currCity=q[0]
                for city in range(len(isConnected[currCity])):
                    if(isConnected[currCity][city]==1 and visited[city]==0):
                        visited[city]=1
                        q.append(city)
                q.popleft()
        visited=[0]*len(isConnected)
        res=0
        for i in range(len(isConnected)):
            if(visited[i]==0):
                BFS(i)
                res+=1
        return res