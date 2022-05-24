class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = [-1]
        ans = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                stk.pop()
                if len(stk) == 0:
                    stk.append(i)
                else:
                    ans = max(ans, i - stk[-1])
                              
        return ans
                