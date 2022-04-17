# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    head, tmp = None, None
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        self.increasingBST(root.left)
        if not self.head:
            self.head = root
            
        if self.tmp:
            root.left = None
            self.tmp.right = root
      
        self.tmp = root

        self.increasingBST(root.right)
        
        return self.head