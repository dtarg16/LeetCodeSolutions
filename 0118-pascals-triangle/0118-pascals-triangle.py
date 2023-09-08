class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        import math
        return [[math.comb(n, m) for m in range(n+1)] for n in range(numRows)]
        
