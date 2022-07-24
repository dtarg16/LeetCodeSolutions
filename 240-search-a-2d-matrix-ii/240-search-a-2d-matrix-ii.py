class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        
        h, w = len(matrix), len(matrix[0])
        
        y, x = h-1, 0
        while True:
            if y < 0 or x >= w:
                break
            current = matrix[y][x]
            
            if target < current:
                y -= 1
            elif target > current:
                x += 1
            else:
                return True
            
        return False