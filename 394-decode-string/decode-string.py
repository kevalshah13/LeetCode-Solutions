class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        count=0
        currStr=''
        ans=''
        for i in s:
            if i.isdigit():
                count=count*10+int(i)
            elif i=='[':
                stack.append((count,currStr))
                count=0
                currStr=''
            elif i==']':
                prev_count,prev_string = stack.pop()
                currStr = prev_string + currStr * prev_count
            else:
                currStr+=i
        return currStr
            