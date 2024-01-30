class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=0
        oper=set('+-*/')
        i=2
        while len(tokens)!=1:
            # print(tokens)
            if tokens[i] in oper:
                if tokens[i]=='+':
                    ans=int(tokens[i-1])+int(tokens[i-2])
                elif tokens[i]=='-':
                    ans=int(tokens[i-2])-int(tokens[i-1])
                elif tokens[i]=='*':
                    ans=int(tokens[i-2])*int(tokens[i-1])
                else:
                    ans=int(int(tokens[i-2])/int(tokens[i-1]))
                tokens[i-2]=ans
                del tokens[i-1]
                del tokens[i-1]
                i=2
            else:
                i+=1
        # print(tokens)
        return int(tokens[0])

        