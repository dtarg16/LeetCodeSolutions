class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = 0

        if k == 0:
            for num in set(nums):
                if nums.count(num) > 1:
                    counter += 1
        else:
            nums = sorted(set(nums))
            d = {}
            for right in nums:
                left = right - k
                left_count = d.get(left, 0)
                if left_count == 1:
                    counter += 1
                    d[left] += 1
                d[right] = d.get(right, 0) + 1
        return counter