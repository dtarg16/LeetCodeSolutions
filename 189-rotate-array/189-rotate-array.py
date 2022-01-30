class Solution(object):
    
    def reverse(self, nums, left, right):
        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1
        
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
#         nums = "------>--->" k =3
#         result = "--->----->"

#         reverse "------>--->"   :   "<---<------"
#         reverse "<---"          :   "---><------"
#         reverse "<------"       :   "--->------>"
        n = len(nums)
        k = k % n
        if k == 0:
            return 
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)