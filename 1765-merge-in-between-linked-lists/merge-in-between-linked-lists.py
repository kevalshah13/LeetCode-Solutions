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
        prev.next=list2
        while(list2.next):
            list2=list2.next
        list2.next=new
        # # print(prev.val,new.val)
        # while(dummy):
        #     if(dummy==prev):
        #         dummy.next=list2
        #         break
        #     else:
        #         dummy=dummy.next
        # # print(dummy)
        
        return head
