class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        self.digits = digits
        self.ans = set()
        
        def rec(sofar):
            if len(sofar) == len(self.digits):
                self.ans.add(sofar)
                return
            
            next_digit = self.digits[len(sofar)]
            for letter in d[next_digit]:
                rec(sofar + letter)
                
        rec("")
        
        return list(self.ans)