class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
                
        def perimeter(mx, nx):
            tmp = []
            for j in range(mx, nx):
                tmp.append((mx, j))
            for i in range(mx + 1, nx):
                tmp.append((i, nx - 1))
            for j in reversed(range(mx, nx - 1)):
                tmp.append((nx - 1, j))
            for i in reversed(range(mx + 1, nx - 1)):
                tmp.append((i, mx))
            return tmp
            
        c, mx, nx = 1, 0, n
        while mx <= nx:
            for i, j in perimeter(mx, nx):
                matrix[i][j] = c
                c += 1
            mx += 1
            nx -= 1
            
        return matrix
            
            
        