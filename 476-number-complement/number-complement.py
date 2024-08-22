class Solution:
    def findComplement(self, num: int) -> int:
        s=''
        while(num>0):
            s+=str(num%2)
            num=num//2
        # print(s)
        # s=s[::-1]
        ns=''
        for i in s:
            if i=='0':
                ns+='1'
            else:
                ns+='0'
        # print(ns)
        ans=0
        for i in range(0,len(ns)):
            ans+=int(ns[i])*(2**i)
            # print(ans)

        return ans