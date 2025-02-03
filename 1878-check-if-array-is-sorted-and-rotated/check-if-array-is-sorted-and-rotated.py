class Solution:
    # def check(self, nums: List[int]) -> bool:
        
        # for i in range(1,len(nums)):
        #     if(nums[i]-nums[i-1]==-1):
        #         return False

    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        inversion_count = 0

        # For every pair, count the number of inversions.
        for index in range(1, n):
            if nums[index] < nums[index - 1]:
                inversion_count += 1

        # Also check between the last and the first element due to rotation
        if nums[0] < nums[n - 1]:
            inversion_count += 1

        return inversion_count <= 1