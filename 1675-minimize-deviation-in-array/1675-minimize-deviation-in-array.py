from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = [i*2 if i%2==1 else i for i in nums]
        sl = SortedList(nums)
        diff = float('inf')
        while sl[-1] % 2 == 0:
            diff = min(diff, sl[-1]-sl[0])
            reduced = int(sl.pop(-1) / 2)
            sl.add(reduced)
        return min(diff, sl[-1]-sl[0])