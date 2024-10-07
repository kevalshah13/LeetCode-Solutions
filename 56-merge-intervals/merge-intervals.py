# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         if len(intervals)<2:
#             return intervals
#         intervals.sort(key=lambda x:x[0])
#         l,r=0,1
#         ans=[]
#         while l<len(intervals):
#             start=intervals[l][0]
#             end=intervals[l][1]
#             while(r<len(intervals) and intervals[l][1]>=intervals[r][0]):
#                 end=max(end,intervals[r][1])
#                 r+=1
#             ans.append([start,end])
#             l=r
#             r=r+1
#         return ans  

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        intervals.sort(key=lambda x:x[0])
        stack=[]
        for i in intervals:
            start=i[0]
            end=i[1]
            if(stack):
                while(stack and i[0]<=stack[-1][1]):
                    start=min(start,stack[-1][0])
                    end=max(end,stack[-1][1])
                    stack.pop()
            stack.append([start,end])
        return stack

            