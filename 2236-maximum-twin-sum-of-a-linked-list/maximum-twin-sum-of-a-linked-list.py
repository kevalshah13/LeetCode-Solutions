# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(head):
            prev,curr=None,head
            while(curr):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        # dummy=ListNode(next=head)
        slow,fast=head,head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        slow=reverse(slow)
        ans=0
        left,right=head,slow
        while(right):
            ans=max(ans,left.val+right.val)
            left=left.next
            right=right.next
        return ans