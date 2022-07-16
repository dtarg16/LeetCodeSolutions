class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
            return sum([solve(x, y, maxMove-1) for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]])

        
        return solve(startRow, startColumn, maxMove) % 1000000007