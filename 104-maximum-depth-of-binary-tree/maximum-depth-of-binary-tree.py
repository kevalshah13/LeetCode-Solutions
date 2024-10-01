# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ans=0
        q=deque()
        q.append((root,1))
        
        while q:
            node,height=q.popleft()
            ans=max(ans,height)
            if node.left:
                q.append((node.left,height+1))
            if node.right:
                q.append((node.right,height+1))
        return ans

