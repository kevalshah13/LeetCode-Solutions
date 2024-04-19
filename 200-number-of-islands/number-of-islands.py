class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            visited[i][j]=1
            for r,c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if(r>=0 and c<n and c>=0 and r<m and visited[r][c]==0 and grid[r][c]=="1"):
                    dfs(r,c)

        m,n=len(grid),len(grid[0])
        visited=[[0 for i in range(n)] for j in range(m)]
        ans=0
        for i in range(m):
            for j in range(n):
                if(visited[i][j]==0 and grid[i][j]=="1"):
                    dfs(i,j)
                    ans+=1
        return ans
        
