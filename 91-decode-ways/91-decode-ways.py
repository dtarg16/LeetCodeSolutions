class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [None] * n
        dp[-1] = int(s[-1] != "0")
        if n == 1:
            return dp[0]
        dp.append(1)
        three_to_nines = [str(x) for x in range(3, 10)]
        seven_to_nines = [str(x) for x in range(7, 10)]
        
        for i in range(n-2, -1, -1):
            if s[i] == "1":
                dp[i] = dp[i+1] + dp[i+2]
            
            elif s[i] == "2":
                if s[i+1] in seven_to_nines:
                    dp[i] = dp[i+1]
                else:
                    dp[i] = dp[i+1] + dp[i+2]
            elif s[i] in three_to_nines:
                dp[i] = dp[i+1]
            else:
                dp[i] = 0
        return dp[0]