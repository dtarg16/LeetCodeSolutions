class Solution:
    
    dp = []
    
    def rec(self, n):
        if n <= 2:
            return n
        if self.dp[n] != -1:
            return self.dp[n]
        
        x = self.rec(n-1) + self.rec(n-2)
        self.dp[n] = x
        return x
    
    def climbStairs(self, n: int) -> int:
        self.dp  = [-1] * (n+1)
        
        return self.rec(n)