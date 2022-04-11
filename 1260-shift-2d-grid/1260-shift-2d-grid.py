class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                j_k = (j + k) % n
                i_k = (j + k) // n
                jj = j_k
                ii  = (i + i_k ) % m        
                ans[ii][jj] = grid[i][j]
        return ans