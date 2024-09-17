class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        mem={}
        ans=[]
        for i in s1.split(' '):
            mem[i]=1+mem.get(i,0)
        # print(mem)
        for i in s2.split(' '):
            mem[i]=1+mem.get(i,0)
        # print(mem)
        for i in mem:
            if mem[i]<2:
                ans.append(i)
        return ans