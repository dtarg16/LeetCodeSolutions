from math import factorial as fact
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return fact(n+4) // (fact(4) * fact(n))
        
            
            
        