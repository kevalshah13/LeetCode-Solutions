class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pre=0
        post=sum(nums)
        ans=0
        for i in range(len(nums)-1):
            post-=nums[i]
            pre+=nums[i]
            if(pre>=post):
                ans+=1
        return ans
        