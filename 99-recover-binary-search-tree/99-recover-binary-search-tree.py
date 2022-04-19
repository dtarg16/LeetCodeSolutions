# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev, self.first, self.second = TreeNode(-pow(2, 31)), None, None
        def rec(root):
            if not root:
                return
            
            rec(root.left)
                
            if self.first is None and self.prev.val > root.val:
                self.first = self.prev
        
            if self.first and self.prev.val > root.val:
                self.second = root
                             
            self.prev = root
            
            rec(root.right)
        
        rec(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val