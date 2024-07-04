# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newAns=0
        ans=dummy=head
        head=head.next
        while(head):
            if(head.val==0):
                # print(head.val,"a")
                dummy.next=ListNode(val=newAns)
                dummy=dummy.next
                newAns=0
            else:
                # print(head.val,"b")
                newAns+=head.val
            head=head.next
        return ans.next