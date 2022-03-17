class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stk = []
        for ch in s:
            if ch == '(':
                stk.append(score)
                score = 0
            else:
                score = stk.pop() + max(score * 2, 1)

        return score
                
        