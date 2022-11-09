class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, p: int) -> int:
        c, s = 1, self.stack
        while s and s[-1][0] <= p:      
            c += s.pop()[1]             
        s.append((p,c)) 
        return c