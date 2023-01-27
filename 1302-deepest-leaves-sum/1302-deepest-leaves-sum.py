# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # base case:
        if root is None:
            return 0
        
        # level order traversal
        q = [root]
        while q:
            cur = []
            for p in q:
                for child in [p.left, p.right]:
                    if child:
                        cur.append(child)
            pre, q = q, cur
        
        # sum values of tree's deepest leaves
        res = 0
        for node in pre:
            res += node.val
        return res
    
        # compact solution:
        # q = [root]
        # while q:
        #     pre, q = q, [child for p in q for child in [p.left, p.right] if child]        
        # return sum(node.val for node in pre)
