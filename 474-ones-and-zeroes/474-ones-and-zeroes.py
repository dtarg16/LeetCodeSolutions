class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [[s.count("0"), s.count("1")] for s in strs]

        @lru_cache(None)
        def dp(mm, nn, index):
            if mm < 0 or nn < 0: 
                return -float('inf')
            
            if index == len(strs): 
                return 0
            
            zeros, ones = counts[index]
            
            x = dp(mm-zeros, nn-ones, index + 1)
            y = dp(mm, nn, index + 1)
            
            return max(x + 1, y)
        
        return dp(m, n, 0)