import collections


def set_bit(n, i):
    return n | 1 << i
class Solution:
    

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        done = (1 << n) - 1
        queue = collections.deque()
        visited = collections.defaultdict(set)
        for i in range(n):
            cur_distance = 0
            cur_vertex = i
            cur_state = 1 << i  # ith bit is showing that we have visited ith vertex
            queue.appendleft((cur_distance, cur_vertex, cur_state))
        # BFS
        while queue:
            cur_dist, cur_vertex, cur_state = queue.pop()
            if cur_state == done:
                return cur_dist
            for next_vertex in graph[cur_vertex]:
                if cur_state not in visited[next_vertex]:
                    visited[next_vertex].add(cur_state)
                    queue.appendleft((cur_dist + 1, next_vertex, set_bit(cur_state, next_vertex)))
        return -1