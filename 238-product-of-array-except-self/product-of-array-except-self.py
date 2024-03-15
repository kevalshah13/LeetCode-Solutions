class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=1
        r=1
        ans=[1]*len(nums)
        for i in range(len(nums)):
            ans[i]*=l
            l=l*nums[i]
            ans[len(nums)-i-1]*=r
            r=r*nums[len(nums)-i-1]
        return ans