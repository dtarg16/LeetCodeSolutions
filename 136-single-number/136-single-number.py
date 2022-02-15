class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        x = 0
        
        for i in range(len(nums)):
            x ^= nums[i]
        return x