# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            # Quick response for empty linked list
            return None
        
        # ------------------------------------------
        # Locate the mid point of linked list
        # First half is the linked list before mid point
        # Second half is the linked list after mid point
        
        fast, slow = head, head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        mid = slow
        
        # ------------------------------------------
        # Reverse second half
        
        prev, cur = None, mid
        
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        head_of_second_rev = prev
        
        # ------------------------------------------
        # Update link between first half and reversed second half
        
        first, second = head, head_of_second_rev
        
        while second.next:
            
            next_hop = first.next
            first.next = second
            first = next_hop
            
            next_hop = second.next
            second.next = first
            second = next_hop
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """

#         dummy=head
#         c=1
#         while(dummy and dummy.next):
#             if(c%2==1):
#                 temp=dummy
#                 mem=dummy.next
#                 while(temp.next and temp.next.next):
#                     temp=temp.next
#                 print(temp.val)
#                 dummy.next=temp.next
#                 print(dummy.next)
#                 print('mem',mem.val)
#                 dummy.next.next=mem
#                 temp.next=None
#             c+=1
#             dummy=dummy.next
#         return head
        # slow=head
        # fast=head
        # while(fast.next):
        #     # l.append(fast.val)
        #     fast=fast.next
        # # print(l)
        # print(fast.val)
        