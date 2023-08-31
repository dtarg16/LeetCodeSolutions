class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n =len(nums)
        dp = [False for i in range(n)]
        dp[0] = True
        
        for i in range(n):
            if dp[i]:
                for j in range(i+1, i+nums[i]+1):
                    if j < n:
                        dp[j] = True
                    if j == n - 1:
                        return True
        return dp[n-1]
                