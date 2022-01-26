class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        
        for i in range(len(nums)):
            x ^= nums[i]
        return x
        