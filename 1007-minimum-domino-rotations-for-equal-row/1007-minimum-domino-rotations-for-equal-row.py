class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)
        top1 = [0] * 7
        bot1 = [0] * 7
        top2 = [0] * 7
        bot2 = [0] * 7
        for i in range(n):
            top1[tops[i]] += 1
            if tops[i] != bottoms[i]:
                bot1[bottoms[i]] += 1
            bot2[bottoms[i]] += 1
            if tops[i] != bottoms[i]:
                top2[tops[i]] += 1
        ans = -1

        for i in range(1, 7):
            if top1[i] + bot1[i] == n:
                if ans == -1:
                    ans = bot1[i]
                else:
                    ans = min(ans, bot1[i])

            if top2[i] + bot2[i] == n:
                if ans == -1:
                    ans = top2[i]
                else:
                    ans = min(ans, top2[i])

        return ans
