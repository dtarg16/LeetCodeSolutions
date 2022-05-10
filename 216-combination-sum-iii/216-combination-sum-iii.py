class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.n = n
        self.k = k
        
        
        def rec(sofar, max_sofar):
            summ = sum(sofar)
            if len(sofar) == self.k:
                if summ == self.n:
                    self.res.append(sofar)
                return
            
            for x in range(max_sofar + 1, max((n - summ, 10))):
                rec(sofar + [x], x)
        
        rec([], 0)
                    
        return self.res
                