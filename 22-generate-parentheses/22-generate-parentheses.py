class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        
        def rec(sofar, open_left, close_left):
            
            if len(sofar) == 2*n:
                self.ans.append(sofar)
                
            if open_left > 0:
                rec(sofar + '(', open_left - 1, close_left + 1)
                
            if close_left > 0:
                rec(sofar + ')', open_left, close_left - 1)
                
        rec('', n, 0)
        
        return self.ans