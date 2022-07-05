class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        
        @lru_cache(None)
        def dp(num):
            if num not in myset:
                return 0
            
            return dp(num-1) + 1
        
        ans = 0
        for num in nums:
            ans = max(ans, dp(num))
            
        return ans