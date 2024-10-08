class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            l,r=i+1,len(nums)-1
            while(l<r):
                if(abs(nums[i])==nums[l]+nums[r]):
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
                elif(nums[l]+nums[r]>abs(nums[i])):
                    r-=1
                else:
                    l+=1
        return ans
        