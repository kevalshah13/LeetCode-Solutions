class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mem={}
        m=0
        c=0
        for i in nums:
            mem[i]=1+mem.get(i,0)
            if(mem[i]>m):
                m=mem[i]
                c=1
            elif(mem[i]==m):
                c+=1
        print(mem,m, c)
        return m*c
        
        