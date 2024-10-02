import heapq
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        arr1 = arr.copy()
        heapq.heapify(arr)
        h = {}
        i = 1

        while len(arr) > 0:
            x = heapq.heappop(arr)

            if x in h: 
                continue
            else:
                h[x] = i

            i += 1

        return [h[x] for x in arr1]