# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val, left=root)
        
        def dfs(node, level):
            if node is None:
                return

            if level == depth - 1:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right = node.right)
                return
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        
        dfs(root, 1)
        
        return root