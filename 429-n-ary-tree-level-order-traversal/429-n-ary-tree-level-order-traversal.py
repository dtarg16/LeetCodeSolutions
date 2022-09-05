"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: 
            return []
        Q, ans = deque([root]), []
        
        while Q:
            level = []
            for i in range(len(Q)):
                node = Q.popleft()
                for child in node.children:
                    Q.append(child)
                level += [node.val] 
            ans += [level]

        return ans