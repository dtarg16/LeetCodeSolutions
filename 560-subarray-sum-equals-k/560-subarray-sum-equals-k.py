class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        count, acc_sum = 0, 0
        freq[0] = 1

        for i in range(len(nums)):
            acc_sum += nums[i]
            count += freq.get(acc_sum - k, 0)
            freq[acc_sum] = freq.get(acc_sum, 0) + 1

        return count