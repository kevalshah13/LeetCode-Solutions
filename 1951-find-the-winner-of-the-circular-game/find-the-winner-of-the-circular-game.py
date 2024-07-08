class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        c=[i for i in range(1,n+1)]
        s=0
        while(len(c)>1):
            count=0
            while(count<k-1):
                s=(s+1)%len(c)
                count+=1
                # print(c,s)
            del c[s]
            # print(c)
        return c[0]

        