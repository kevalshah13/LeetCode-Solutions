class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)
        # while(k>0):
        #     nums.insert(0,nums.pop())
        #     k-=1
            # print(nums)
        bisect=k%len(nums)
        nums[:]=nums[-bisect:]+nums[:-bisect]
        # nums=a
        return nums