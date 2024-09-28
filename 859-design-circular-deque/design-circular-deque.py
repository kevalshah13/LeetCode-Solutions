class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = None
        self.rear = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head is None:
            self.head = Node(value, None, None)
            self.rear = self.head
        else:
            newHead = Node(value, self.head, None)
            self.head.prev = newHead
            self.head = newHead

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head is None:
            self.head = Node(value, None, None)
            self.rear = self.head
        else:
            self.rear.next = Node(value, None, self.rear)
            self.rear = self.rear.next

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None
            self.rear = None
        else:
            self.head = self.head.next

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None
            self.rear = None
        else:
            self.rear = self.rear.prev

        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# class ListNode:
#     def __init__(self,val=0,next=None,prev=None):
#         self.val=val
#         self.next=None
#         self.prev=None

# class MyCircularDeque:
#     def __init__(self, k: int):
#         self.c=0
#         self.l=None
#         self.r=None
#         self.k=k

#     def insertFront(self, value: int) -> bool:
#         if c<k:
#             self.c+=1
#             if self.r:
#                 self.r.prev=ListNode(value)
#                 self.r=self.r.next 
#                 return True
#             else:
#                 self.l=ListNode(value)
#                 self.r=ListNode(value)
#         else:
#             return False
        
#     def insertLast(self, value: int) -> bool:
#         if c<k:
#             self.c+=1
#             if self.l:
#                 new=ListNode(value,next=self.l)
#                 self.l=new
#                 return True
#             else:
#                 self.l=ListNode(value)
#                 self.r=ListNode(value)
#         else:
#             return False


#     def deleteFront(self) -> bool:
        

#     def deleteLast(self) -> bool:
#         if(self.l):
#             self.l=self.l.next
#             return True
#         else:
#             return False

#     def getFront(self) -> int:
        

#     def getRear(self) -> int:
#         return self.l.val

#     def isEmpty(self) -> bool:
#         return self.l or self.r

#     def isFull(self) -> bool:
#         return c==k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()