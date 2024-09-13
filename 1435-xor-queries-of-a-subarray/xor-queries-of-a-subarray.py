class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix_XOR = [0] * (n + 1)

        # Build prefix XOR array
        for i in range(n):
            prefix_XOR[i + 1] = prefix_XOR[i] ^ arr[i]

        ans=[]
        for i in queries:
            ans.append(prefix_XOR[i[1]+1]^prefix_XOR[i[0]])
            # l=i[0]
            # res=arr[l]
            # while l<i[1]:
            #     res=res^arr[l+1]
            #     l+=1
            # ans.append(res)
        return ans
        