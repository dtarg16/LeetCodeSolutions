# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

COVERED_WITHOUT_CAMERA = 2
LEAF = 0
PARENT_OF_LEAF_WITH_CAMERA = 1
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root):
            if not root: 
                return COVERED_WITHOUT_CAMERA
            
            l, r = dfs(root.left), dfs(root.right)
            if l == LEAF or r == LEAF:
                self.res += 1
                return PARENT_OF_LEAF_WITH_CAMERA
            
            if l == PARENT_OF_LEAF_WITH_CAMERA or r == PARENT_OF_LEAF_WITH_CAMERA:
                return COVERED_WITHOUT_CAMERA
            else:
                return LEAF
        
        return (dfs(root) == LEAF) + self.res