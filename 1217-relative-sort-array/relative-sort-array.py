class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mem={}
        for i in arr1:
            mem[i]=1+mem.get(i,0)
        ans=[]
        for i in arr2:
            if i in mem:
                for j in range(mem[i]):
                    ans.append(i)
                del mem[i]
        a=sorted(mem)
        for i in a:
            for j in range(mem[i]):
                ans.append(i)
        # print(ans)
        # print(mem)
        return ans
        