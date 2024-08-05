class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mem={}
        for i in arr:
            mem[i]=1+mem.get(i,0)
        for i in mem:
            if(mem[i]==1):
                k-=1
                if(k==0):
                    return i
        return ""