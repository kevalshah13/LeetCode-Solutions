# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count=set()
        while(head):
            if head in count:
                return True
            count.add(head)
            head=head.next
        return False
        