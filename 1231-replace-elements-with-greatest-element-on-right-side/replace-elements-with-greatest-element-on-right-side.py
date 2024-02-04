class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[-1]*len(arr)
        m=arr[-1]
        for i in range(len(arr)-1,0,-1):
            m=max(m,arr[i])
            ans[i-1]=m
        return ans