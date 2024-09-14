class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mem=0
        m=max(nums)
        if(len(nums)<2):
            return 1
        l,r=0,1
        while(r<len(nums)):
            # curr=1
            while(r<len(nums) and nums[l]==m and nums[l]==nums[r]):
                # curr+=1
                r+=1
            mem=max(mem,r-l)
            # print(l,r,mem)
            l=r
            r+=1
        return mem