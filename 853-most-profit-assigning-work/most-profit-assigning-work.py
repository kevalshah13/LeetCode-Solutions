class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        hmap=[]
        for i in range(len(profit)):
            hmap.append((profit[i],difficulty[i]))
        hmap.sort(reverse=True)
        # print(hmap)
        worker.sort(reverse=True)
        ans=0
        for i in worker:
            for j in hmap:
                if i>=j[1]:
                    ans+=j[0]
                    break
        return ans
        