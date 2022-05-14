from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        grid = [[-1] * (n + 1) for _ in range(n + 1)]

        for u, v, w in times:
            grid[u][v] = w

        maxx = 0
        visited = []
        pq = []
        heappush(pq, (0, k))

        while pq:
            time, node = heappop(pq)
            if node in visited:
                continue
            visited.append(node)
            maxx = max(maxx, time)
            if len(visited) == n:
                return maxx
            for neighbour in range(1, n + 1):
                time_cost = grid[node][neighbour]
                if neighbour != node and time_cost != -1 and not neighbour in visited:
                    heappush(pq, (time + time_cost, neighbour))

        return -1
        