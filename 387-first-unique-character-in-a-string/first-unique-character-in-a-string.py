class Solution(object):
    def firstUniqChar(self, s):
        mem={}
        a=-1
        for i in s:
            mem[i]=1+mem.get(i,0)
        for i in mem:
            if mem[i]==1:
                a=i
                break
        if a==-1:
            return a
        else:
            return s.index(a)
