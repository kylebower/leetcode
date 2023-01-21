# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        
        # recursivley find max depth
        left_depth = 0
        right_depth = 0
        if root.left:
            left_depth = self.maxDepth(root.left)
        if root.right:
            right_depth = self.maxDepth(root.right)
        max_depth = 1 + max(left_depth, right_depth)
        
        # return max depth
        return max_depth
        