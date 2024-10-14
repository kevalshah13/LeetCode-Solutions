import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums=[-x for x in nums]
        heapq.heapify(nums)
        ans=0
        for i in range(k):
            curr=heapq.heappop(nums)
            ans-=curr
            heapq.heappush(nums,curr//3)
        return abs(ans)