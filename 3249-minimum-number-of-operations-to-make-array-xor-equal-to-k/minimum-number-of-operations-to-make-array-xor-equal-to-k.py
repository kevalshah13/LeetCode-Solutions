class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.append(k)
        return reduce(xor,nums).bit_count()