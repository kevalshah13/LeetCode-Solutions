class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mem={}
        for i in arr:
            mem[i]=1+mem.get(i,0)
        # print(mem)
        mem=dict(sorted(mem.items(), key=lambda i: i[1]))
        for i in mem:
            if(k>=mem[i]):
                k-=mem[i]
                mem[i]=0
            else:
                break
        # print(mem)
        ans=0
        for i in mem:
            if mem[i]!=0:
                ans+=1
        return ans