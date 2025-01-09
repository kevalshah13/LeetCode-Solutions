class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n=len(prefix)
        ans=0
        for i in words:
            if i.startswith(pref):
                ans+=1
        return ans