class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        def rec(n):
            if n in memo:
                return memo[n]
            memo[n] = rec(n-1) + rec(n-2)
            return memo[n]

        return rec(n)
