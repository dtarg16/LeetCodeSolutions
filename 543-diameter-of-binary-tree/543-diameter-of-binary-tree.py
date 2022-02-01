# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def rec(self, root):
        if root is None:
            return -1
        
        left, right = self.rec(root.left), self.rec(root.right)
        self.diameter = max(self.diameter, left + right + 2)
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.rec(root)
        return self.diameter