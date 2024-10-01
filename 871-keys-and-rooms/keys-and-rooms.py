from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[0]*len(rooms)
        q=deque([0])
        visited[0]=1
        while q:
            currRoom=q[0]
            for key in rooms[currRoom]:
                if visited[key]==0:
                    visited[key]=1
                    q.append(key)
            q.popleft()
        return sum(visited)==len(rooms)

