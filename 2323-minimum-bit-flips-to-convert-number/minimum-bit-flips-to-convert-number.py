class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n=start ^ goal
        ans=0
        while(n>0):
            if(n%2==1):
                ans+=1
            n=n//2
        return ans
        