"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.ans = []
        
        def rec(root):
            if not root:
                return 
            
            self.ans.append(root.val)
            
            for node in root.children:
                rec(node)
                
        rec(root)
        
        return self.ans