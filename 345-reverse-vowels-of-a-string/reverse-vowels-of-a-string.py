class Solution:
    def reverseVowels(self, s: str) -> str:
        mem=[]
        ans=''
        for i in s:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                mem.append(i)
        # print(mem)
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                ans+=mem.pop()
            else:
                ans+=s[i]
        return ans
        