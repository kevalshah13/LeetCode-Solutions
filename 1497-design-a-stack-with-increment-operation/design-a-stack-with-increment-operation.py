from collections import deque

class CustomStack:

    def __init__(self, maxSize: int):
        self.q=deque()
        self.c=0
        self.size=maxSize

    def push(self, x: int) -> None:
        if(self.c<self.size):
            self.q.append(x)
            self.c+=1

    def pop(self) -> int:
        if(self.q):
            self.c-=1
            return self.q.pop()
        return -1        

    def increment(self, k: int, val: int) -> None:
        if(k<self.c):
            for i in range(k):
                self.q[i]+=val
        else:
            for i in range(self.c):
                self.q[i]+=val

            


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)