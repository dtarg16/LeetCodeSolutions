class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                middle = (left + right) // 2
                if target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
            return left
        
        l, r = bs(nums, target - 0.5), bs(nums, target + 0.5)
        if l == r:
            return [-1, -1]
        
        return [l, r - 1]
        
        