# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        c=0
        dummy=head=list1
        while(list1):
            if(c+1==a):
                prev=list1
                # print('p',list1.val)
            if(c-1==b):
                new=list1
                # print(list1.val)
            c+=1
            list1=list1.next
        # # print(prev.val,new.val)
        while(dummy):
            if(dummy==prev):
                dummy.next=list2
                break
            else:
                dummy=dummy.next
        # print(dummy)
        while(dummy.next):
            dummy=dummy.next
        dummy.next=new
        return head
