
def is_between(area, current):
    start, end = area
    r1, c1 = start
    r2, c2, = end
    r, c = current
    return r1 <= r <= r2 and c1 <= c <= c2

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dig_grid = [[0] * n for _ in range(n)]
        for r, c in dig:
            dig_grid[r][c] = 1

        counter = 0

        for r1, c1, r2, c2 in artifacts:

            all_dig = True
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if dig_grid[i][j] == 0:
                        all_dig = False
                        break

            if all_dig:
                counter += 1

        return counter