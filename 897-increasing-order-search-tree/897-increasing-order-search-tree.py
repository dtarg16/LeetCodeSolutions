# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rec(self, root):
        if not root:
            return None
        
        left = self.rec(root.left)
        self.arr.append(root.val)
        right = self.rec(root.right)
        
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.arr = []
        self.rec(root)
        head = TreeNode(self.arr[0])
        tmp = head
        for i in range(1, len(self.arr)):
            tmp.right = TreeNode(self.arr[i])
            tmp = tmp.right
        return head
        
    