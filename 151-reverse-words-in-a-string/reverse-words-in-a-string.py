class Solution:
    def reverseWords(self, s: str) -> str:
        i=0
        words=[]
        while i<len(s):
            st=''
            while i<len(s) and s[i]!=' ':
                st+=s[i]
                i+=1
            if(st):
                words.append(st)
            i+=1
        return ' '.join(words[::-1])