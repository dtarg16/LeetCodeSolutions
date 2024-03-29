class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def helper(i, k, c):
            
            if i < 0 and k <= 1: 
                return 0
            if k > i + 1 or k < 1: 
                return math.inf
            if houses[i] and c != houses[i]: return math.inf
            
            paint_cost = cost[i][c - 1] * (not houses[i])
            prev_cost = min(helper(i - 1, k, c), min([helper(i - 1, k - 1, c_) \
                    for c_ in range(1, n + 1) if c_ != c] or [math.inf]))
            
            return paint_cost + prev_cost
        
        res = min(helper(m - 1, target, c) for c in range(1, n + 1))
        
        return res if res < math.inf else -1