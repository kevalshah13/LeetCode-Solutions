class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=0
        l,r=0,0
        countZero=0
        while(r<len(nums)):
            if(nums[r]==0):
                countZero+=1
            r+=1
            if(countZero>1):
                if nums[l]==0:
                    countZero-=1
                l+=1
            
        return r-l-1
