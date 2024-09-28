class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod,n=10**9+7,len(arr)
        oddSum,evenSum,currSum,ans=0,1,0,0
        for i in arr:
            currSum+=i
            if currSum%2==1:
                oddSum+=1
                ans+=evenSum%mod
            else:
                evenSum+=1
                ans+=oddSum%mod
        return ans%mod   