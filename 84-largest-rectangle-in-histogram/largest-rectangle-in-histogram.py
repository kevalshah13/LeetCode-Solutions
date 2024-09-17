class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[]
        for i,h in enumerate(heights):
            start=i
            while(stack and stack[-1][1]>h):
                maxArea=max(maxArea,stack[-1][1]*(i-stack[-1][0]))
                start=stack[-1][0]
                stack.pop()
            stack.append([start,h])
            # print(stack)
        for i,h in stack:
                maxArea=max(maxArea,h*(len(heights)-i))
        return maxArea
