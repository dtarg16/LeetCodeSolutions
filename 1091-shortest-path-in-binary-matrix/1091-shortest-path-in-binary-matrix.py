from heapq import heappop, heappush

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def in_grid(i, j):
            return 0 <= i < n and 0 <= j < n
        
        visited = [[0] * n for _ in range(n)]
        q = []
        if grid[0][0] == 0:
            heappush(q, (1, 0, 0))
            visited[0][0] = 1
        
        while q:
            w, i, j = heappop(q)
            
            if i == n-1 and j == n-1:
                return w
            
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ni, nj = i + di, j + dj
                    if in_grid(ni, nj) and grid[ni][nj] == 0 and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        heappush(q, (w + 1, ni, nj))
        return -1
                    
            
            