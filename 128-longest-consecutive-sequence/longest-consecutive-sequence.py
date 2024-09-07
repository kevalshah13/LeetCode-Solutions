class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = {}  # Dictionary to store the longest sequence ending at each number
        max_length = 0
        
        for num in nums:
            if num not in dp:  # Only process if the number hasn't been processed before
                # Get the length of the sequence ending at num - 1
                left = dp.get(num - 1, 0)
                # Get the length of the sequence starting at num + 1
                right = dp.get(num + 1, 0)
                
                # Current sequence length is left + 1 (num itself) + right
                current_length = left + 1 + right
                
                # Update the dictionary with the current sequence length
                dp[num] = current_length
                dp[num - left] = current_length  # Update the start of the sequence
                dp[num + right] = current_length  # Update the end of the sequence
                
                # Update the maximum sequence length
                max_length = max(max_length, current_length)
        
        return max_length