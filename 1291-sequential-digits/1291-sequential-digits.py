class Solution:
    
    def sequentialDigitsStartingWith(self, n: int, low:int, high:int) -> List[int]:
        numbers = []
        number = n
        while number <=high:
            if number >= low:
                numbers.append(number)
            n += 1
            if n > 9 : break
            number = number * 10 + n
        return numbers
    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        
        for i in range(1,10):
            ans += self.sequentialDigitsStartingWith(i, low, high)
            
        return sorted(ans)