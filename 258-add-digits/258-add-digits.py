class Solution:
    
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        remainder = num % 9
        if remainder == 0:
            remainder = 9
        return remainder