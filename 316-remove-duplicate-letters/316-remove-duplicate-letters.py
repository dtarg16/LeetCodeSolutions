class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {}
        for i in range(len(s)):
            ch = s[i]
            last_occur[ch] = i

        stk = []
        for i in range(len(s)):
            ch = s[i]

            if ch not in stk:
                while stk:
                    last_ch = stk[-1]
                    if last_ch > ch and last_occur[last_ch] > i:
                        stk.pop()
                    else:
                        break
                stk.append(ch)

        return ''.join(stk)