# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # base case
        if original == None or original == target:
            return cloned
        
        node = self.getTargetCopy(original.left, cloned.left, target)
        if node:
            return node
        else:
            return self.getTargetCopy(original.right, cloned.right, target)
    