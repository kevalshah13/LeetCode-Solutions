class MovingAverage:

    def __init__(self, size: int):
        self.q=collections.deque()
        self.sum=0
        self.size=size
        self.length=0

    def next(self, val: int) -> float:
        if(self.length<self.size):
            self.q.append(val)
            self.sum+=val
            self.length+=1         
        else:
            l=self.q.popleft()
            self.sum=self.sum-l+val
            self.q.append(val)
        return self.sum/self.length

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)