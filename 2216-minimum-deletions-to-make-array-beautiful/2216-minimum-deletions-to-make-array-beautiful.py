class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        counter = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
                counter += 1
            else:
                i += 2
        if len(nums) % 2 == 0:
            return counter
        else:
            return counter + 1