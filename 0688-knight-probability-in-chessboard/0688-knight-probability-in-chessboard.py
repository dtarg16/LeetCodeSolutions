class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if abs(i) != abs(j) and i*j != 0 ]

        visited = {}

        def dp(row, col, n, k):
            if k<0:
                return 1
            elif (row < 0 or row >= n) or (col < 0 or col >= n):
                return 0
            elif (row, col, k) in visited:
                return visited[(row, col, k)]

            prob = sum(dp(row + i, col + j, n, k - 1) * 1/8 for i, j in moves)
            visited[(row, col, k)] = prob
            return prob

        return dp(row, column, n, k)