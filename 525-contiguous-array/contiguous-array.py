class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mem={}
        sumVal=0
        ans=0
        for i in range(len(nums)):
            sumVal+=1 if nums[i]==1 else -1
            if sumVal==0:
                ans=i+1
            elif sumVal in mem:
                ans=max(ans,i-mem[sumVal])
            else:
                mem[sumVal]=i
        return ans