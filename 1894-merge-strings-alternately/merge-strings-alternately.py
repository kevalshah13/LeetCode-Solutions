class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=''
        i=0
        while(i<len(word1) and i<len(word2)):
            ans+=word1[i]+word2[i]
            i+=1
        # if(word1):
        ans+=word1[i:] or word2[i:]
        return ans
        
