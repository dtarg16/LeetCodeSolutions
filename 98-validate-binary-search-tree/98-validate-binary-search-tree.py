# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(root, floor, ceiling):
            if not root: 
                return True
            if root.val <= floor or root.val >= ceiling:
                return False
            
            left = rec(root.left, floor, root.val)
            right = rec(root.right, root.val, ceiling)
            
            return left and right
        
        return rec(root, -float('inf'), float('inf'))