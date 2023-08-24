class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i, factors = 1, 0
        while i <= n:
            if n % i == 0:
                factors += 1
            
            if factors == k:
                return i
            i += 1
        return -1