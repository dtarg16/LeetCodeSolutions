class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0:cost[0], 1:cost[1]}
        m = len(cost)

        def rec(n):
            if n in memo:
                return memo[n]
            memo[n] = min(rec(n-1), rec(n-2)) + cost[n]
            return memo[n]

        return min(rec(m-1), rec(m-2))