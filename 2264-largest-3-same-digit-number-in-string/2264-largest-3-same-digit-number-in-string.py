class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in reversed(range(0, 10)):
            x = str(digit) * 3
            if num.find(x) != -1:
                return x

        return ""