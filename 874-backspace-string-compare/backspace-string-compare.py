class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def Compare(st):
            stack=[]
            for i in st:
                if(stack and i=='#'):
                    stack.pop()
                elif(i!='#'):
                    stack.append(i)
            return stack
        print(Compare(s))
        print(Compare(t))
        return Compare(s)==Compare(t)