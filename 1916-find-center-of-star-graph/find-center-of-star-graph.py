class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree=[0]*(len(edges)+2)
        for i in edges:
            degree[i[0]]+=1
            degree[i[1]]+=1
        ans=0
        m=0
        # print(degree)
        for i in range(1,len(degree)):
            if(degree[i]>m):
                m=degree[i]
                ans=i
        return ans
        