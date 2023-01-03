# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output_list = []
        output_list.append(root.val)
        if root.left:
            left_val = self.preorderTraversal(root.left)
            output_list += left_val
        if root.right:
            right_val = self.preorderTraversal(root.right)
            output_list += right_val
        return output_list
        