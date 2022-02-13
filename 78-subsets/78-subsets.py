class Solution:
    def __init__(self):
        self.ps = []
        self.nums = []

    def rec(self, i, sofar):
        if i == len(self.nums):
            self.ps.append(sofar)
        else:
            self.rec(i + 1, sofar)
            self.rec(i + 1, sofar + [self.nums[i]])

    def subsets(self, nums):
        self.ps = []
        self.nums = nums
        self.rec(0, [])
        return self.ps