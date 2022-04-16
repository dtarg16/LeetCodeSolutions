# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(root, sofar):
            if not root:
                return sofar
            right = traverse(root.right, sofar)
            left = traverse(root.left, root.val + right)
            root.val = root.val + right
            return left
        
        traverse(root, 0)
        return root
            
            