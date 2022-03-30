class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix[0]), len(matrix)
        l, r = 0, m * n - 1
        while l <= r:

            mid = l + (r - l) // 2

            x, y = mid // m, mid % m

            if matrix[x][y] == target:
                return True

            elif matrix[x][y] < target:
                l = mid + 1

            else:
                r = mid - 1

        return False 
        