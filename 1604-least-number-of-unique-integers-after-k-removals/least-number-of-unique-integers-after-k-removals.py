class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mem={}
        for i in arr:
            mem[i]=1+mem.get(i,0)
        mem=dict(sorted(mem.items(), key=lambda i: i[1]))
        ans=len(mem)
        for i in mem:
            k-= mem[i]
            if k<0:
                break
            ans-=1
        
            # if(k>=mem[i]):
            #     k-=mem[i]
            #     mem[i]=0
            # else:
            #     break
        # ans=0
        # for i in mem:
        #     if mem[i]!=0:
        #         ans+=1
        return ans