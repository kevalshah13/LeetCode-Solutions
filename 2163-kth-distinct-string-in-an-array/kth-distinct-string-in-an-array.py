class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mem={}
        for i in arr:
            mem[i]=1+mem.get(i,0)
        c=0
        for i in mem:
            if(mem[i]==1):
                c+=1
                if(c==k):
                    return i
        return ""