# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, isLeft):
            # base case
            if not root:
                return 0

            # compute left leaf sum
            if not root.left and not root.right:
                return root.val if isLeft else 0

            # recursive call
            return dfs(root.left, True) + dfs(root.right, False)
        
        return dfs(root, False)
    