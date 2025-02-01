class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        else:
            for i in range(1,len(nums)):
                if((nums[i-1]%2==0 and nums[i]%2==0) or (nums[i-1]%2==1 and nums[i]%2==1)):
                    return False
        return True
        