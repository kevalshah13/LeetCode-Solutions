class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if(i=='+'):
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
            elif(i=='*'):
                a=stack.pop()
                b=stack.pop()
                stack.append(a*b)
            elif(i=='-'):
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif(i=='/'):
                a=stack.pop()
                b=stack.pop()
                if(b/a<0):
                    ans=math.ceil(b /a)
                else:
                    ans=b//a
                stack.append(ans)
            else:
                stack.append(int(i))
            # print(stack)
        return stack[-1]