# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.visited = 0
        self.ans = -1
        
        def rec(root):
            if not root:
                return 
            
            rec(root.left)
            self.visited += 1
            if self.visited == k:
                self.ans = root.val
                return 
            rec(root.right)
        
        rec(root)
        return self.ans
        