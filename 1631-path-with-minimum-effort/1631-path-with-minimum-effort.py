class Solution:

    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m, n = len(heights), len(heights[0])
        scores = [[float('inf')] * n for _ in range(m)]
        h = []
        score, i, j = 0, 0, 0
        heappush(h, (score, i, j))
        while h:
            score, i, j = heappop(h)
            if score > (scores[i][j]):
                continue
            if i == m - 1 and j == n - 1:
                return score

            for delta_i in range(-1, 2):
                for delta_j in range(-1, 2):
                    if delta_j != delta_i and delta_j * delta_i == 0:
                        ii, jj = i + delta_i, j + delta_j
                        if 0 <= ii < m and 0 <= jj < n:
                            new_score = max(score, abs(heights[ii][jj] - heights[i][j]))
                            if new_score < scores[ii][jj]:
                                scores[ii][jj] = new_score
                                heappush(h, (new_score, ii, jj))