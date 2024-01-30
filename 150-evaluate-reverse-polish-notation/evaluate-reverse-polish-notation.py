class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=0
        oper=set('+-*/')
        i=2
        if len(tokens)<2:
            return int(tokens[0])
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
                    ans=int(tokens[i-2])/int(tokens[i-1])
                    if ans<0:
                        ans=ceil(ans)
                    else:
                        ans=floor(ans)
                tokens[i-2]=ans
                del tokens[i-1]
                del tokens[i-1]
                i=2
            else:
                i+=1
        # print(tokens)
        return tokens[0]

        