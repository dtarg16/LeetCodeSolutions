class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row_glass = [[0] * 101 for i in range(101)]
        row_glass[0][0] = poured
        for i in range(query_row):
            for j in range(100):
                rem = max(row_glass[i][j] - 1, 0)
                row_glass[i+1][j] += rem / 2
                row_glass[i+1][j+1] += rem / 2
        return min(row_glass[query_row][query_glass], 1)