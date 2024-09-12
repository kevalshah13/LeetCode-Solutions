from collections import defaultdict
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        c=0
        for i in words:
            flag=1
            for j in i:
                if j not in allowed:
                    flag=0
            if flag==1:
                c+=1
        return c