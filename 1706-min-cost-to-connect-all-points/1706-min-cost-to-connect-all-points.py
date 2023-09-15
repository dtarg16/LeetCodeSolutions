class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1: List[int], p2: List[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        visited = [False] * n
        heap_dict = {0: 0}  
        min_heap = [(0, 0)]
        
        mst_weight = 0
        
        while min_heap:
            weight, point = heappop(min_heap)
            
            if visited[point] or heap_dict.get(point, float('inf')) < weight:
                continue
            
            visited[point] = True
            mst_weight += weight
            
            for next_point in range(n):
                if visited[next_point]:
                    continue
                
                new_distance = manhattan_distance(points[point], points[next_point])
    
                if new_distance < heap_dict.get(next_point, float('inf')):
                    heap_dict[next_point] = new_distance
                    heappush(min_heap, (new_distance, next_point))
        
        return mst_weight

