class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if abs(i) != abs(j) and i*j != 0 ]


        @cache
        def dp(row, col, k):
            if not(0 <= row < n and 0 <= col < n):
                return 0
            
            if k==0:
                return 1

            return sum(dp(row + i, col + j, k - 1) * 1/8 for i, j in moves)


        return dp(row, column, k)