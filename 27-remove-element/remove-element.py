class Solution:
    def removeElement(self, nums, val):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] == val:
                # Swap the current element with the element at r
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1  # Decrement r since we want to ignore this position
            else:
                l += 1  # Only increment l if we did not swap
        
        return l  # Length of the array without the removed elements


        # print(nums)