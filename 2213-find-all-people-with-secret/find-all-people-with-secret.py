import heapq
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Create a graph to represent the meetings
        graph = defaultdict(list)
        for x, y, time in meetings:
            graph[x].append((time, y))
            graph[y].append((time, x))

        # Add the firstPerson to the graph with time 0
        graph[0].append((0, firstPerson))
        graph[firstPerson].append((0, 0))

        # Use a priority queue to process meetings in chronological order
        pq = [(0, 0), (0, firstPerson)]
        visited = set()

        while pq:
            time, person = heapq.heappop(pq)
            if person in visited:
                continue
            visited.add(person)

            # Share the secret with all people at the current time
            for next_time, next_person in graph[person]:
                if next_person not in visited and next_time >= time:
                    heapq.heappush(pq, (next_time, next_person))

        return list(visited)