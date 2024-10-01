from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)

        r_arr = deque([i for i in range(len(senate)) if senate[i]=='R'])
        d_arr = deque([j for j in range(len(senate)) if senate[j]=='D'])
        
        while r_arr and d_arr:
            r = r_arr.popleft()
            d = d_arr.popleft()
            if r < d:
                r_arr.append(n + r)
            else:
                d_arr.append(n + d)
                
        return 'Radiant' if r_arr else 'Dire'