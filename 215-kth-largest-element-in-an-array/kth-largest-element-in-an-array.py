import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=nums[:k]
        heapq.heapify(heap)
        for i in range(k,len(nums)):
            last=heapq.heappop(heap)
            if(nums[i]>last):
                heapq.heappush(heap,nums[i])
            else:
                heapq.heappush(heap,last)
        return heapq.heappop(heap)