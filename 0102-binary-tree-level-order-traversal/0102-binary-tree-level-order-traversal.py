# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base case
        if root is None:
            return []
        
        result = []
        
        # perform breadth-first-search
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()                
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            result.append(level)
        
        # return the level order traversal of its nodes' values
        return result