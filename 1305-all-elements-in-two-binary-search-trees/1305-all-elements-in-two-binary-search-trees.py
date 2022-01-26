# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    left, right = [], []

    def traverse(self, node, is_left):
        if node:
            self.traverse(node.left, is_left)
            if is_left:
                self.left.append(node.val)
            else:
                self.right.append(node.val)
            self.traverse(node.right, is_left)
            
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.left, self.right = [], []
        self.traverse(root1, 1)
        self.traverse(root2, 0)
        my_list = []
        print(self.left, self.right)
        i, j, k = 0, 0, 0

        while i < len(self.left) and j < len(self.right):
            if self.left[i] <= self.right[j]:
                my_list.append(self.left[i])
                i += 1
            else:
                my_list.append(self.right[j])
                j += 1

        while i < len(self.left):
            my_list.append(self.left[i])
            i += 1
            k += 1

        while j < len(self.right):
            my_list.append(self.right[j])
            j += 1
            k += 1
        return my_list
