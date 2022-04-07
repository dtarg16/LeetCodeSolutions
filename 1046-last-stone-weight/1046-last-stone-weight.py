from heapq import heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        h = []
        for stone in stones:
            heappush(h, -stone)

        while len(h) > 1:
            x, y = heappop(h), heappop(h)
            if x != y:
                heappush(h, x - y)
        if h:
            return -h[0]
        return 0