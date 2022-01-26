class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cum_sums = nums
        for i in range(1, len(nums)):
            self.cum_sums[i] = self.cum_sums[i - 1] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        r = self.cum_sums[right]
        l = self.cum_sums[left-1] if left > 0 else 0
        return r - l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)