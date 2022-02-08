class Solution:
    
    def addDigits(self, num: int) -> int:
        if num:
            return num % 9 or 9
        else:
            return 0