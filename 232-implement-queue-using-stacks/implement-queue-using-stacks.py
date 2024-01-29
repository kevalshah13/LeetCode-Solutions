class MyQueue:

    def __init__(self):
        self.main=[]
        self.temp=[]

    def push(self, x: int) -> None:
        while self.main:
            self.temp.append(self.main.pop())
        
        self.main.append(x)

        while self.temp:
            self.main.append(self.temp.pop())

    def pop(self) -> int:
        # del self.l[-1]
        return self.main.pop()
    def peek(self) -> int:
        return self.main[-1]

    def empty(self) -> bool:
        return not self.main

# class MyQueue:

#     def __init__(self):
#         self.l=[]

#     def push(self, x: int) -> None:
#         self.l.append(x)

#     def pop(self) -> int:
#         # del self.l[-1]
#         return self.l.pop(0)
#     def peek(self) -> int:
#         return self.l[0]

#     def empty(self) -> bool:
#         return len(self.l)==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()