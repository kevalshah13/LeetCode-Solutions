class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp=[1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if(nums[i]%nums[j]==0):
                    dp[i]=max(dp[i],1+dp[j])
        m=max(dp)
        prev=dp.index(m)
        ans=[]
        for i in range(len(dp)-1,-1,-1):
            if(dp[i]==m and nums[prev]%nums[i]==0):
                ans.append(nums[i])
                m-=1
                prev=i
        return ans




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ans=defaultdict(list)
        # for i in range(len(nums)):
        #     temp=[]
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]%nums[j]==0 or nums[j]%nums[i]==0):
        #             temp.append(nums[j])
        #     ans[nums[i]]=temp
        # print(ans)
        # res=[nums[0]]
        # visited=[0]*(max(ans)+1)
        # def dfs(i):
        #     visited[i]=1
        #     if not ans[i]:
        #         return res
        #     for j in ans[i]:
        #         if visited[j]==0:
        #             res.append(j)
        #             print(dfs(j))
        # dfs(nums[0])
        # print(res)

                 
        # return []