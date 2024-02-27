# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         def dfs(node):
#             if not node:
#                 return 0
#             return 1+max(dfs(node.left),dfs(node.right))
#         return dfs(root.left)+dfs(root.right)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # Update the diameter by considering the path that passes through the current node
            self.diameter = max(self.diameter, left_depth + right_depth)

            # Return the depth of the current subtree
            return 1 + max(left_depth, right_depth)

        self.diameter = 0
        dfs(root)
        return self.diameter

