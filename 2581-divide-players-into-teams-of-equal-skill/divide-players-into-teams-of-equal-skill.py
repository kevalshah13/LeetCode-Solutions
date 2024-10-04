class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        skills.sort()
        ans=0
        l,r=0,len(skills)-1
        while(l<r):
            if(l==0):
                ans+=skills[l]*skills[r]
                prevSum=skills[l]+skills[r]
            if(l!=0 and skills[l]+skills[r]==prevSum):
                ans+=skills[l]*skills[r]
                prevSum=skills[l]+skills[r]
            if(skills[l]+skills[r]!=prevSum):
                return -1
            l+=1
            r-=1
        return ans