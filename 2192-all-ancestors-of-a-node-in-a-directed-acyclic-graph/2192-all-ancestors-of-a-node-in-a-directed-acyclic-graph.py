class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        vertex_neighbours = defaultdict(list)

        for frm, to in edges:
            vertex_neighbours[frm].append(to)

        ancestors = [[] for i in range(n)]
        # visited = set()

        def dfs(vertex, visited):
            for to_vertex in vertex_neighbours[vertex]:
                if to_vertex in visited:
                    continue
                ancestors[to_vertex].append(i)
                visited.add(to_vertex)
                dfs(to_vertex, visited)
        i = 0
        while i < n:
            dfs(i, set())
            i += 1
        return ancestors
        