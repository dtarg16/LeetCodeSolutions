class Solution:
    def romanToInt(self, s: str) -> int:
        s_v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        stk = []
        res = 0
        for symbol in s:
            value = s_v[symbol]
            while stk and value > stk[-1]:
                    res -= stk.pop()
            stk.append(value)

        return res + sum(stk)