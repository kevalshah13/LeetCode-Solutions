# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        while(head and head.next):
            b=head.next
            new=self.GCD(head.val,b.val)
            head.next=ListNode(val=new,next=b)
            head=b
        return dummy
    def GCD(self,a,b):
        if(b == 0):
            return a
        else:
            return self.GCD(b, a % b)