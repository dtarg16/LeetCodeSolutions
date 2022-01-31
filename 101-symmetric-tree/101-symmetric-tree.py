# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rec(self, left, right):
        if not (left or right):
            return True
        if left and right:
            return left.val == right.val and self.rec(left.right, right.left) and self.rec(left.left, right.right)
        
        return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root.left, root.right)