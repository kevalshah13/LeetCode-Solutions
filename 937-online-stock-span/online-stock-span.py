class StockSpanner:

    def __init__(self):
        self.stack=[]
        
    def next(self, price: int) -> int:
        currSpan=1
        while self.stack and self.stack[-1][0]<=price:
            currSpan+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,currSpan))
        return currSpan

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)