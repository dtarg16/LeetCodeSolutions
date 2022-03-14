# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    
    def bst_root(self, low, high):
        
        if low == high:
            return TreeNode(self.nums[low])
        if low > high:
            return None;
  
        mid = (low + high)//2
            
        return TreeNode(self.nums[mid], self.bst_root(low, mid-1), self.bst_root(mid+1, high))

        
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        
        return self.bst_root(0, len(nums) - 1)