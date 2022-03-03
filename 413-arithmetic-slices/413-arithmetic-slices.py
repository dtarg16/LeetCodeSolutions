class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n, ans = 0, 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                n += 1
            else:
                ans += n * (n + 1) // 2
                n = 0
        ans += n * (n + 1) // 2
        return ans