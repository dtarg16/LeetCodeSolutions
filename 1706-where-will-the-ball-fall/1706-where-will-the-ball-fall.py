class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        def check(row,col):
            if row==m:
                return col
            new_col = col+grid[row][col]
            if new_col==n or new_col==-1 or grid[row][new_col]!=grid[row][col]:
                return -1
            else:
                return check(row+1,new_col)
        res = []
        for i in range(n):
            res.append(check(0,i))
        return res