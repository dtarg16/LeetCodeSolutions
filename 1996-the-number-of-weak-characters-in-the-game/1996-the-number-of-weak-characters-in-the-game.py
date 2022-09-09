class Solution:
    def numberOfWeakCharacters(self, X: List[List[int]]) -> int:
        X = sorted(X)
        n = len(X)
        ans, d, max_y = 0, defaultdict(list), -1
 
        for a, b in X:
            d[a] += [b]
            
        for t in sorted(list(d.keys()))[::-1]:
            for q in d[t]:
                if q < max_y: ans += 1
            for q in d[t]:
                max_y = max(max_y, q)
                
        return ans