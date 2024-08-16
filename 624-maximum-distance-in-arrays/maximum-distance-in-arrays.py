# from collections import defaultdict
# class Solution:
#     def maxDistance(self, arrays: List[List[int]]) -> int:
#         mem=defaultdict(list)
#         for i in range(len(arrays)):
#             mem[i].append(min(arrays[i]))
#             mem[i].append(max(arrays[i]))
#         print(mem)
#         ans=0
#         mem=dict(sorted(mem.items(), key=lambda item: item[1][1]))
#         keys = list(mem.keys())

#         for i in range(len(keys)-1):
#             ans=max(ans,abs(mem[keys[i]][0]-mem[keys[i+1]][1]),abs(mem[keys[i+1]][0]-mem[keys[i]][1]))
#         return ans

class Solution(object):
    def maxDistance(self, arrays):
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return max_distance
        