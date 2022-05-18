class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        current_rank = 0
        lowest_rank = [i for i in range(n)]

        visited = [False for _ in range(n)]

        res = []
        prev_vertex = -1

        u = 0
        self.dfs(res, graph, lowest_rank, visited, current_rank, prev_vertex, u)
        return res

    def dfs(self, res, graph, lowest_rank, visited, current_rank, prev_vertex, u):
        visited[u] = True
        lowest_rank[u] = current_rank

        for v in graph[u]:
            if v == prev_vertex:
                continue

            if not visited[v]:
                self.dfs(res, graph, lowest_rank, visited, current_rank + 1, u, v)

            lowest_rank[u] = min(lowest_rank[u], lowest_rank[v])

            if lowest_rank[v] >= current_rank + 1:
                res.append([u, v])
