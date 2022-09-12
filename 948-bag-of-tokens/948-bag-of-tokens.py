class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        max_ans = score = 0
        
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                max_ans = max(max_ans, score)
                l += 1
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                break
        
        return max_ans