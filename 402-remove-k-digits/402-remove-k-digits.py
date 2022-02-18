class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'

        stk = []
        for ch in num:
            while k and stk and stk[-1] > ch:
                stk.pop()
                k -= 1

            stk.append(ch)

        while k:
            k -= 1
            stk.pop()

        i = 0
        while True:
            if i == len(stk):
                return '0'
            if stk[i] == '0':
                i += 1
            else:
                return ''.join(stk[i:])