# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans=[[-1 for i in range(n)] for j in range(m)]
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        cdir=0
        r,c=0,0
        while head is not None:
            ans[r][c]=head.val
            newr=r+dir[cdir][0]
            newc=c+dir[cdir][1]
            if(min(newr,newc)<0 or newr>=m or newc>=n or ans[newr][newc]!=-1):
                cdir=(cdir+1)%4
            r+=dir[cdir][0]
            c+=dir[cdir][1]

            head=head.next
        # return ans
        # for i in range(m*n):
        #     if(r<m):
        #         if(c<n):
        #             if(head):
        #                 ans[r][c]=head.val
        #                 head=head.next
        #             c+=1
        #         else:
        #             cdir=(cdir+1)%4
        #             curr=dir
        #         r+=1
        return ans
        