class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans=0
        currScore=0
        l,r=0,len(tokens)-1
        if len(tokens)==1:
            if tokens[0]<power:
                return 1
            else:
                return 0
        while(l<=r):
            if currScore==0:
                if tokens[l]>power:
                    break
                else:
                    currScore+=1
                    power-=tokens[l]
                    l+=1
            else:
                if tokens[l]>power:
                    power+=tokens[r]
                    currScore-=1
                    r-=1
                else:
                    currScore+=1
                    power-=tokens[l]
                    l+=1
            ans=max(ans,currScore)
        # print(ans)
        return ans

        