class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 4:
            return n == 1
        
        if n % 4 != 0:
            return False
        
        return self.isPowerOfFour(n // 4)