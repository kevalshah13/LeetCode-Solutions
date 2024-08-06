class Solution:
    def minimumPushes(self, word: str) -> int:
        available=8
        mem={}
        for i in word:
            mem[i]=1+mem.get(i,0)
        if(len(mem)<=8):
            return len(word)
        mem = dict(sorted(mem.items(), key=lambda x: x[1],reverse=True))
        ans=0
        count=0
        # mult=1
        for i in mem:
            # if(count>=8):
            #     count=count%8
            #     mult+=1
            ans+=mem[i]*(count//8 +1)
            count+=1
        return ans