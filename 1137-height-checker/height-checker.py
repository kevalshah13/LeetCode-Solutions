class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h=sorted(heights)
        print(h)
        ans=0
        for i in range(len(heights)):
            if h[i]!=heights[i]:
                ans+=1
        
        # for i in range(len(heights)-1):
        #     if(heights[i+1]<heights[i]):
        #         ans+=1
        return ans
        