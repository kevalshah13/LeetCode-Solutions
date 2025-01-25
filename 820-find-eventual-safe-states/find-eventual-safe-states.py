class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        status=[0]*(n)
        res=[]
        
        def dfs(i):
            if status[i]==1: 
                return True
            if status[i]==2: 
                return False
            status[i]=1 
            for j in graph[i]:
                if  dfs(j):
                    return True
            status[i]=2 
            return False      
    
        for i in range(n):
            if not dfs(i): 
                res.append(i)
        return res
            
        
        return tnode
        