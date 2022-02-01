class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        first_zero = 0
        first_non_zero = 0
        while True:
            while nums[first_zero] != 0:
                first_zero += 1
                if first_zero == len(nums):
                    return 
                
            while nums[first_non_zero] == 0 or first_non_zero < first_zero:
                first_non_zero += 1
                if first_non_zero == len(nums):
                    return 
            
            nums[first_zero], nums[first_non_zero] = nums[first_non_zero], nums[first_zero]
            