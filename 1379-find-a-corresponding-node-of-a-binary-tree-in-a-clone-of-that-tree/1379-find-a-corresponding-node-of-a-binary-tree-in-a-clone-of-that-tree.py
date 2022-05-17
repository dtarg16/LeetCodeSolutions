# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def rec(node):
            if not node:
                return False
            
            if node == target:
                return True
            
            left, right = rec(node.left), rec(node.right)
            
            if left:
                self.path.append(0)
            elif right:
                self.path.append(1)
                
            return left or right
        
        self.path = []
        rec(original)
        for i in self.path[::-1]:
            if i == 0:
                cloned = cloned.left
            else:
                cloned = cloned.right
                
        return cloned
                
            