class Solution:
    def frequencySort(self, s: str) -> str:
        count={}
        for i in s:
            count[i]=1+count.get(i,0)
        # print(count)
        sort = [[] for _ in range(len(s) + 1)]
        for i,n in count.items():
            sort[n].append(i)
        # print(sort)
        ans=''
        for i in range(len(sort)-1,0,-1):
            j=0
            while(sort[i]):
                ans+=sort[i][j]*i
                del sort[i][j]
        # print(ans)
        # print(sort)
        return ans
        