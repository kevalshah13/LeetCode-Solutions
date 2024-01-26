class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in mem:
                return [mem[diff],i]
            else:
                mem[n]=i

