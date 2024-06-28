class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree=[0]*(n)
        for i in roads:
            indegree[i[0]]+=1
            indegree[i[1]]+=1
        # print(indegree)
        indegree.sort()
        ans=0
        for i in range(0,len(indegree)):
            ans+=indegree[i]*(i+1)
        return ans

        