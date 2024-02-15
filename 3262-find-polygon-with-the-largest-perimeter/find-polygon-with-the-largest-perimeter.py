class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,2
        ans=0
        curr=sum(nums[:2])
        while(r<len(nums)):
            if(nums[r]<curr):
                ans=curr+nums[r]
            curr+=nums[r]
            r+=1
        if ans==0:
            return -1
        else:
            return ans

        