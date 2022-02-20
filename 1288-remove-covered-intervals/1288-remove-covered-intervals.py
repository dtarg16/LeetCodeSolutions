class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda i: (i[0], -i[1]))
        ans, right_most = 0, 0

        for left, right in intervals:

            if right > right_most:
                right_most = right
                ans += 1

        return ans