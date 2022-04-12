# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def rec(root, sofar):
            if not root:
                return False
            
            if not (root.left or root.right):
                return sofar == root.val
            
            left, right = rec(root.left, sofar - root.val), rec(root.right, sofar - root.val)
            return left or right
        
        return rec(root, targetSum)