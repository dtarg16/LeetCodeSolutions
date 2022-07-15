class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
                grid[i][j] = 0
                ans = 1
                for x , y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    ans += sink(x, y)
                return ans
            return 0
        return max(sink(i, j) for i in range(m) for j in range(n))