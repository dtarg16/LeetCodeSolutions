class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}

        def rec(n):
            if n in memo:
                return memo[n]
            memo[n] = rec(n-1) + rec(n-2) + rec(n-3)
            return memo[n]

        return rec(n)