class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        d = {}
        def check(i, j):
            if not (i, j) in d:
                tmp = 0
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        tmp = max(tmp, check(x, y))
                    
                d[(i, j)] = tmp + 1
                
            return d[(i, j)]
        
        
        return max(check(i, j) for i in range(m) for j in range(n))