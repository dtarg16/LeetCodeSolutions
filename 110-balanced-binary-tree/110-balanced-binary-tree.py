# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rec(self, root):
        if root is None:
            return 0
            
        right = self.rec(root.right)
        left = self.rec(root.left)
            
        if left == -1 or right == -1:
            return -1
            
        if abs(right-left) > 1:
            return -1
            
        return 1 + max(left, right)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
            
        return self.rec(root) != -1