class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[]
        
        for i in spells:
            l,r=0,len(potions)-1
            while(l<=r):
                mid=(l+r)//2
                # print(mid)
                if(i*potions[mid]>=success):
                    r=mid-1
                else:
                    l=mid+1
            ans.append(len(potions)-r-1)
        return ans   