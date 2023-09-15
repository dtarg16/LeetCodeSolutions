class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1, s2 = list(map(ord, s1)), list(map(ord, s2))
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(m)] for _ in range(n)]   
        for j, i in product(range(m), range(n)):
            dp[i][j] = max((j>0) * dp[i][j-1], 
                           (i>0) * dp[i-1][j], 
                           (s1[j] == s2[i]) * ((i>0 and j >0) * dp[i-1][j-1] + s1[j]))
        return sum(s1) + sum(s2) - 2 * dp[-1][-1]