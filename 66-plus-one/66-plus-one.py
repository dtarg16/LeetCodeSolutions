class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        
        while digits[index] == 9:
            digits[index] = 0
            index -= 1
        
        if(index < 0):
            digits = [1] + digits
        else:
            digits[index] += 1
            
        return digits