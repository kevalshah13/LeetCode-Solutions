class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [p for p in nums if p > 0]
        neg = [n for n in nums if n < 0]
        ans = []
        for p, n in zip(pos, neg):
            ans += [p, n]
        return ans

# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         pos=[]
#         neg=[]
#         for i in nums:
#             if(i>0):
#                 pos.append(i)
#             else:
#                 neg.append(i)
#         ans=[]
#         while(len(nums)>len(ans)):
#             ans.append(pos[0])
#             del pos[0]
#             ans.append(neg[0])
#             del neg[0]
#         return ans