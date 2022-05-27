class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num <= 1:
            return num
        
        if num % 2 == 1:
            return 1 + self.numberOfSteps(num-1)
        else:
            return 1 + self.numberOfSteps(num//2)