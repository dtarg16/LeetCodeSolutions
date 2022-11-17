class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        def getHeight(node,side):
            if not node: return 1
            return getHeight(node.left,side)+1 if side=='l' else getHeight(node.right,side)+1
        
        l = getHeight(root.left,'l')
        r = getHeight(root.right,'r')
        if l==r: return pow(2,l) - 1
        return self.countNodes(root.left)+self.countNodes(root.right) + 1