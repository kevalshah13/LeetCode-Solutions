class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        types=set()
        for i in candyType:
            types.add(i)
        return min(len(types),n//2)