class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        curr=0
        for i in arr:
            if(i%2==1):
                curr+=1
            else:
                curr=0
            if(curr==3):
                return True
        return False