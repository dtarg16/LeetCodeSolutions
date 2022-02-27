# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, node, level, x):
        if node is None:
            return

        if level not in self.left:
            self.left[level] = x

        self.maxx = max(self.maxx, x - self.left[level] + 1)
        self.rec(node.left, level + 1, x * 2)
        self.rec(node.right, level + 1, x * 2 + 1)

    def widthOfBinaryTree(self, root) -> int:
        self.left = {}
        self.right = {}
        self.maxx = 1
        self.rec(root, 0, 0)
        return self.maxx
        
        