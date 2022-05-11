class Solution:
    def countVowelStrings(self, n: int) -> int:
        self.d = {1: 'a', 2:'e', 3:'i', 4:'o', 5:'u'}
        self.n = n
        self.res = 0
        
        def rec(sofar, last_index):
            if len(sofar) == n:
                self.res += 1
                return
            
            for i in range(last_index, 6):
                rec(sofar + self.d.get(i), i)
                
        rec("", 1)
        
        return self.res
        