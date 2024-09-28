class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        
        # Calculate the sum of the first k elements
        curr = sum(nums[:k])
        ans = curr
        
        # Sliding window logic
        l, r = 0, k - 1
        while r < len(nums) - 1:
            r += 1
            curr = curr - nums[l] + nums[r]  # Update the sliding window
            l += 1
            ans = max(ans, curr)  # Now compare after updating the window
        
        return ans / k
