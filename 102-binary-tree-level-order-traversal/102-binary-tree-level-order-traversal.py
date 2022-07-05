# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans, queue = [], [root]
        
        while queue:
            tmp = []
            for i in range(len(queue)):
                tmp_node = queue.pop(0)
                tmp.append(tmp_node.val)
                
                if tmp_node.left:
                    queue.append(tmp_node.left)
                
                if tmp_node.right:
                    queue.append(tmp_node.right)
                    
            ans.append(tmp)
            
        return ans