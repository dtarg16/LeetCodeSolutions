class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1: List[int], p2: List[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        points, distance, weight = [tuple(point) for point in points], {}, 0
        
        for point in points:
            distance[point] = float('inf')

        distance[points[0]] = 0
        
        while distance:
            point = min(distance, key=distance.get)
           
            weight += distance.pop(point)
            
            for next_point in distance:
                distance[next_point] = min(distance[next_point], manhattan_distance(point, next_point))
        
        return weight



        
