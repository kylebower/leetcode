"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        # define output list
        output = []
        
        # perform breadth-first-search
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                for child in curr.children:
                    q.append(child)
                level.append(curr.val)
            output.append(level)
        
        # return list
        return output