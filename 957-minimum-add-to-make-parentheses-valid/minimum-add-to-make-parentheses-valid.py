class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if stack:
                if(i==')' and stack[-1]=='('):
                    stack.pop()
                    continue
            stack.append(i)
        return len(stack)