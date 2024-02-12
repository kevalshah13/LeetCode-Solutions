class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mem={}
        for i in nums:
            if i in mem:
                mem[i]+=1
            else:
                mem[i]=1
            if(mem[i]>len(nums)/2):
                return i
        return 0