class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre=[0]
        post=[0]
        for i in range(len(nums)-1):
            pre.append(pre[-1]+nums[i])
        for j in range(len(nums)-1,0,-1):
            post.append(post[-1]+nums[j])
        for i in range(len(pre)):
            if(pre[i]==post[len(post)-1-i]):
                return i
        return -1
        

