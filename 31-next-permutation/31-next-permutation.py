class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        latest_peak, n = 0, len(nums)
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                latest_peak = i
                
        if latest_peak == 0:
            nums.reverse()
            return
        
        pre_peak, min_after_peak = latest_peak - 1, latest_peak
        
        for i in range(latest_peak, n):
            if nums[i] > nums[pre_peak] and nums[i] < nums[min_after_peak]:
                min_after_peak = i
          
        nums[pre_peak], nums[min_after_peak] = nums[min_after_peak], nums[pre_peak]
        
        nums[latest_peak:] = sorted(nums[latest_peak:])