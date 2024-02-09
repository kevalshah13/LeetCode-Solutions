class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp=[1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if(nums[i]%nums[j]==0):
                    dp[i]=max(dp[i],1+dp[j])
        # print(dp)
        m=max(dp)
        prev=dp.index(m)
        ans=[]
        for i in range(len(dp)-1,-1,-1):
            if(dp[i]==m and nums[prev]%nums[i]==0):
                ans.append(nums[i])
                m-=1
                prev=i
        # print(ans)

        return ans
        # l,r=0,0
        # while(r<len(nums)):
        #     while(l<r):
        #         if(nums[l]%nums[r]==0 or nums[r]%nums[l]==0):
        #             dp[nums[r]].append(nums[l])
        #         l+=1
        #     print(l,r)
        #     r+=1
        #     l=0
            
        
        print(dp)
        # for i in nums:
        #     for j in range(1,i+1):
        #         if(i%j==0 or j%i==0):
        #             dp[i].append(j)
        # print(dp)
        # ans=0
        # m=0
        # for i in nums:
        #     if(len(dp[i])>m):
        #         ans=dp[i]
        #         m=len(dp[i])
        # print(ans)
        return []




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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