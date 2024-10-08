class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans=0
        curr=0
        for i in nums:
            curr+=i
            if(curr==0):
                ans+=1
        return ans