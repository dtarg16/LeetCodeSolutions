class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
                
        
        c = 1
        mx, nx = 0, n
        while mx <= nx:
            for j in range(mx, nx):
                matrix[mx][j] = c
                c += 1
            for i in range(mx + 1, nx):
                matrix[i][nx-1] = c
                c += 1
            for j in reversed(range(mx, nx - 1)):
                matrix[nx-1][j] = c
                c += 1
            for i in reversed(range(mx + 1, nx - 1)):
                matrix[i][mx] = c
                c += 1
            mx += 1
            nx -= 1
            
        return matrix
            
            
        