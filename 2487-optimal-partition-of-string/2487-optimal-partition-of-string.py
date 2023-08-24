class Solution:
    def partitionString(self, s: str) -> int:
        visited = []
        count = 1

        for ch in s:
            if ch in visited:
                visited = [ch]
                count += 1
            else:
                visited.append(ch)

        return count
