class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        minn, maxx = min(nums), max(nums)
        num_sum = [0] * (maxx + 1)
        for num in nums:
            num_sum[num] += num

        prev_max, curr_max = 0, 0
        for i in range(minn, maxx + 1):
            prev_max, curr_max = curr_max, max(prev_max + num_sum[i], curr_max)
        return curr_max