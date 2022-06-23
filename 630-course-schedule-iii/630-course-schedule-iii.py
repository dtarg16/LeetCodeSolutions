class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        heap, time = [], 0
        
        for duration, last_day in courses:
            time += duration
            heapq.heappush(heap, -duration)
            
            if time > last_day:
                negative_time = heapq.heappop(heap)
                time += negative_time
                
        return len(heap)