# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        level={root:0}
        def helper(root):
            if(root is None):
                return None
            if root.left:
                level[root.left]=1+level[root]
                helper(root.left)
            if root.right:
                level[root.right]=1+level[root]
                helper(root.right)
        helper(root)
        # print(level)
        ans=root.val
        m=0
        for i in level:
            if(level[i]>m):
                ans=i.val
                m=level[i]
        return ans
            