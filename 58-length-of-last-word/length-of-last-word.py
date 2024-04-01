class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==1:
            return 1
        c=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                c+=1
            elif s[i]==" " and c!=0:
                return c
        return c