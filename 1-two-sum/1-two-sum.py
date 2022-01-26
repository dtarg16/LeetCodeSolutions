class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indeces = {}
        for i in range(len(nums)):
            num = nums[i]
            j = indeces.get(target - num, -1)
            if  j != -1 and i != j:
                return [i, j] 
            indeces[num]=i
            