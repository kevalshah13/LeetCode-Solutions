class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        curr=0 
        for i in s:
            if(i=='('):
                curr+=1
            elif(i==')'):
                curr-=1
            ans=max(ans,curr)
        return ans
        