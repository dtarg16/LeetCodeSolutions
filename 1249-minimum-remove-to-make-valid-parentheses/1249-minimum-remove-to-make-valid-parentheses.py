class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        tmp = ''
        counter = 0

        for ch in s:
            if ch == ')' and counter == 0:
                continue
            if ch == ')':
                counter -= 1
            if ch == '(':
                counter += 1
            tmp += ch
        ans = ''
        for i in range(len(tmp)-1, -1, -1):
            ch = tmp[i]
            if ch == '(' and counter > 0:
                counter -= 1
            else:
                ans = ch + ans

        return ans