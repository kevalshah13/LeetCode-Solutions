class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)-extraCandies
        ans=[]
        for i in candies:
            if i>=m:
                ans.append(True)
            else:
                ans.append(False)
        return ans 