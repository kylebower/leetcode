# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return self.dfs(root, 0)
    
    def dfs(self, root, depth):
        if root.left is None and root.right is None:
            return depth+1
        else:
            if root.left and root.right:
                return min(self.dfs(root.left, depth+1), self.dfs(root.right, depth+1))
            elif root.left:
                return self.dfs(root.left, depth+1)
            else:
                return self.dfs(root.right, depth+1)
    