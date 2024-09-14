# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         mem=0
#         m=max(nums)
#         if(len(nums)<2):
#             return 1
#         l,r=0,1
#         while(r<len(nums)):
#             while(r<len(nums) and nums[l]==m and nums[l]==nums[r]):
#                 r+=1
#             mem=max(mem,r-l)
#             l=r
#             r+=1
#         return mem
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = ans = current_streak = 0
        for num in nums:
            if max_val < num:
                max_val = num
                ans = current_streak = 0

            if max_val == num:
                current_streak += 1
            else:
                current_streak = 0

            ans = max(ans, current_streak)
        return ans