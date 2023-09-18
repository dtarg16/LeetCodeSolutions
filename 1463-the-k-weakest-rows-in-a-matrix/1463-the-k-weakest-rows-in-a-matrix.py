class Solution:
    def kWeakestRows(self, matrix: List[List[int]], k: int) -> List[int]:
        min_heap = []

        for row in range(len(matrix)):
            soldier_count = self.find_soldier_count(matrix[row])
            heapq.heappush(min_heap, (soldier_count, row))

        weakest_rows = []
        for i in range(k):
            weakest_rows.append(heapq.heappop(min_heap)[1])

        return weakest_rows

    def find_soldier_count(self, row):
        left, right = 0, len(row) - 1

        while left <= right:
            mid = (left + right) // 2
            if row[mid] == 1:
                left = mid + 1
            else:
                right = mid - 1

        return left