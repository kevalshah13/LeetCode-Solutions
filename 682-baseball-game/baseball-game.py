class Solution:
    def calPoints(self, ops: List[str]) -> int:
        mem=[]
        for i in range(len(ops)):
            if ops[i]=='+':
                mem.append(mem[-2]+mem[-1])
            elif ops[i]=='D':
                mem.append(mem[-1]*2)
            elif ops[i]=='C':
                del mem[-1]
            else:
                mem.append(int(ops[i]))
            # print(ops[i],mem)
        return sum(mem)

        