class MyCalendarTwo:

    def __init__(self):
        self.single_booked = []
        self.double_booked = []

    def book(self, start: int, end: int) -> bool:
        # first check for a overlap interval in double booked
        for booking in self.double_booked:
            s, e = booking[:]
            if start < e and end > s:
                return False
        for booking in self.single_booked: 
            s, e = booking[:]
            if start < e and end > s:
                self.double_booked.append((max(s, start), min(e, end)))
        self.single_booked.append((start, end)) 
        return True
# class MyCalendarTwo:

#     def __init__(self):
#         self.single=[]
#         self.double=[]
        
#     def book(self, start: int, end: int) -> bool:
#         for i in self.double:
#             if start<i[1] and end>i[0]:
#                 return False
#         for i in self.single:
#             if(start<=i[1] and end>i[0]):
#                 self.double.append((max(i[0],start),min(i[1],end)))
#         self.single.append((start,end))
#         return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)