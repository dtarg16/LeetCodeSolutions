class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] + [float('inf') for i in range(amount)]
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
                else:
                    break
                    
        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]
            