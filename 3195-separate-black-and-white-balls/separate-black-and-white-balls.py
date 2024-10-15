class Solution:
    def minimumSteps(self, s: str) -> int:
        ones=[]
        for i in range(len(s)):
            if s[i]=='1':
                ones.append(i)
        r=len(s)-1
        ans=0
        for l in range(len(ones)-1,-1,-1):
            ans+=(r-ones[l])
            r-=1
        return ans