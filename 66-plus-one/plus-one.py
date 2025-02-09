class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=0
        for i in digits:
            ans=ans*10+i
        ans+=1
        res=collections.deque()
        while(ans>0):
            res.appendleft(ans%10)
            ans=ans//10
        return list(res)
