# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        dummy=head
        n=0
        while(dummy):
            n+=1
            dummy=dummy.next
        length=[n//k]*k
        rem=n%k
        ans=[]
        for i in range(rem):
            length[i]+=1
        for i in range(k):
            j=length[i]
            dummy1=new=head
            while(j>1):
                head=head.next
                new.next=head
                new=new.next
                j-=1
            if head:
                head=head.next
            if new:
                new.next=None
            ans.append(dummy1)
        return ans
        # [ListNode(val=0)]
        