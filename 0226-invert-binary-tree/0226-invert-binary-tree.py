# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root_left_old = root.left
        root_right_old = root.right
        root.left = self.invertTree(root_right_old)
        root.right = self.invertTree(root_left_old)
        return root