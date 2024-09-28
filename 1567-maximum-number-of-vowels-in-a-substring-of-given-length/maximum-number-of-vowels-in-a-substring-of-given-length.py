class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiou')
        vowelCount=[0]*(len(s))
        ans=0
        curr=0
        for i in range(len(s)):
            curr+=s[i] in vowels
            if i>=k:
                curr-=s[i-k] in vowels
            # ans=max(ans,curr)
            # curr=curr-vowelCount[i-1]+int(s[i+k-1] in vowels)
            # vowelCount[i+k-1]
            ans=max(ans,curr)
        return ans

