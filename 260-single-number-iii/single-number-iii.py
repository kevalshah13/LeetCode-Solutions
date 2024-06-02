class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mem={}
        for i in nums:
            mem[i]=1+mem.get(i,0)
        print(mem)
        ans=[]
        for i in mem:
            if mem[i]==1:
                ans.append(i)
        return ans
        