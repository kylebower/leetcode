# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        
        # compute left leaf sum
        sum_left_leaves = 0
        if root.left and not root.left.left and not root.left.right:
            sum_left_leaves += root.left.val
            
        # recursive call
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) + sum_left_leaves
    