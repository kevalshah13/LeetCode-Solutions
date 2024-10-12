class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=len(nums)+1
        l,r=0,0
        total=0
        while(r<len(nums)):
            total+=nums[r]
            while(total>=target):
                ans=min(ans,r-l+1)
                total-=nums[l]
                l+=1
            r+=1
        return ans if ans!=len(nums)+1 else 0