class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1,i2=0,0
        ans=''
        while(i1<len(word1) and i2<len(word2)):
            ans+=word1[i1]
            ans+=word2[i2]
            i1+=1
            i2+=1
        if i1<len(word1):
            ans+=word1[i1:]
        if i2<len(word2):
            ans+=word2[i2:]
        return ans