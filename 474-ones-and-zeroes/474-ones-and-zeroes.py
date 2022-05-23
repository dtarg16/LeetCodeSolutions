class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [[s.count("0"), s.count("1")] for s in strs]

        @lru_cache(None)
        def dp(m_rem, n_rem, index):
            if m_rem < 0 or n_rem < 0: 
                return -float('inf')
            
            if index == len(strs): 
                return 0
            
            zeros, ones = counts[index]
            
            x = dp(m_rem-zeros, n_rem-ones, index + 1)
            y = dp(m_rem, n_rem, index + 1)
            
            return max(x + 1, y)
        
        return dp(m, n, 0)