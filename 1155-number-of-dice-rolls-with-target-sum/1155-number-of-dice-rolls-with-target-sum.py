class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if k * n < target: 
            return 0
        elif  k * n == target:
            return 1
        dp = [[0] * (target+1) for _ in range(n)]
        modulo = 1000000007 
        for i in range(1, min(k+1, target+1)): 
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(i, target+1):
			    # The maximum sum that the dices can roll is (i+1) * k
                if j > (i+1) * k: break
                for m in range(1, k+1):
                    if j - m <= 0: break
                    dp[i][j] += dp[i-1][j-m]
        return dp[n-1][target] % modulo