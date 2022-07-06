class Solution:
    def fib(self, n: int) -> int:
        self.dp = {}
        
        def rec(n):
            if n <= 1:
                return n
            if n in self.dp.keys():
                return self.dp[n]
            else:
                res = rec(n-1) + rec(n-2)
                self.dp[n] = res
                return res
            
        return rec(n)
