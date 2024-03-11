class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # mem={}
        # for i in range(len(order)):
        #     mem[order[i]]=i
        # mem = dict(sorted(mem.items(), key=lambda x:x[1]))
        count={}
        for i in s:
            count[i]=1+count.get(i,0)
        # print(mem)
        # print(count)
        ans=''
        for i in order:
            if i in count:
                ans+=i*count[i]
                del count[i]
        for i in count:
            ans+=i*count[i]
        # print(count)
        return ans
        