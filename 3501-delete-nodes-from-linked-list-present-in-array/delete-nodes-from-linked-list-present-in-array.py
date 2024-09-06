# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ans=ListNode(next=head)
        nums_set = set(nums)
        while(dummy and dummy.next):
            while(dummy.next and dummy.next.val in nums_set):
                dummy.next=dummy.next.next
            dummy=dummy.next
        return ans.next

        