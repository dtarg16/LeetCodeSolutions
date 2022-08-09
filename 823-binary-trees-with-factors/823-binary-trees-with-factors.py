class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        s_arr, N = set(arr), 10**9 + 7
        
        @lru_cache(None)
        def dp(num):
            ans = 1
            for cand in s_arr:
                if num % cand == 0 and num//cand in s_arr:
                    ans += dp(cand)*dp(num//cand)
            return ans
        
        return sum(dp(num) for num in s_arr) % N