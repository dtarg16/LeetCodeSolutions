class Solution:
    def canCross(self, stones: List[int]) -> bool:
        m = {}  # stone positions to indices
        n = len(stones)
        dp = [[-1] * n for _ in range(n)]

        def solve(i, k):
            if i == n - 1:
                return True

            if dp[i][k] != -1:
                return dp[i][k] == 1

            k0, kp, k1 = False, False, False

            if stones[i] + k in m:
                k0 = solve(m[stones[i] + k], k)
            if k > 1 and stones[i] + k - 1 in m:
                kp = solve(m[stones[i] + k - 1], k - 1)
            if stones[i] + k + 1 in m:
                k1 = solve(m[stones[i] + k + 1], k + 1)

            dp[i][k] = 1 if k0 or kp or k1 else 0
            return dp[i][k] == 1

        if stones[1] - stones[0] != 1:
            return False

        for i in range(n):
            m[stones[i]] = i

        return solve(1, 1)