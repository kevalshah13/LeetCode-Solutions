class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        q=collections.deque()
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==2):
                    q.append((i,j))
        if not q and any(1 in row for row in grid):
            return -1
        
        # If there are no oranges at all, return 0
        if not any(1 in row for row in grid) and not q:
            return 0
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        time=-1
        while q:
            time+=1
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    if((r+dr) in range(m) and (c+dc) in range(n) and grid[r+dr][c+dc]==1):
                        grid[r+dr][c+dc]=2
                        q.append((r+dr,c+dc))
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    return -1
        return time
                    
                