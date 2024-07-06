# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # cr=[]
        index=[]
        i=1
        prev=head
        head=head.next
        while(head.next):
            if((head.val>prev.val and head.val>head.next.val) or (head.val<prev.val and head.val<head.next.val)):
                # cr.append(head)
                index.append(i)
            prev=head
            head=head.next
            i+=1
        # print(index)
        if len(index)>1:
            ans=sum(index)
            for i in range(1,len(index)):
                ans=min(index[i]-index[i-1],ans)
            return [ans,index[-1]-index[0]]
        return [-1,-1]
        