class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        l, i = len(nums), 0
        while True and i < l - 2:
            if nums[i] == nums[i+2]:
                i += 3
            else:
                return nums[i]

        return nums[i]