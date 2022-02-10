class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0

        acc_sum = [0] * (len(nums) + 1)
        counter = 0
        for i in range(len(nums)):
            acc_sum[i + 1] = acc_sum[i] + nums[i]

        freq_sum = {}
        for acc in acc_sum:
            counter += freq_sum.get(acc - k, 0)
            freq_sum[acc] = freq_sum.get(acc, 0) + 1
        return counter