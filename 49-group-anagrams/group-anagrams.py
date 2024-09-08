from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem=defaultdict(list)
        for i in strs:
            arr=[0]*26
            for j in i:
                arr[ord(j)-ord('a')]+=1
            mem[tuple(arr)].append(i)
        return mem.values()
        