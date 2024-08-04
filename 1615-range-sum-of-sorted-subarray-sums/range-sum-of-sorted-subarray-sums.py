class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr=[]
        for i in range(n):
            curr=nums[i]
            arr.append(curr)
            for j in range(i+1,n):
                curr+=nums[j]
                arr.append(curr)
        # print(arr)
        arr.sort()
        # print(arr)
        ans=0
        right=min(right,len(arr))
        # print("r",right)
        for i in range(left-1,right):
            ans=(ans+arr[i]) % (10**9 + 7)
            # print(i)
        return ans

        