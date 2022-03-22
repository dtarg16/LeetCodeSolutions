class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        num_val = {}
        for ch_ord in range(ord('a'), ord('z') + 1):
            num_val[ch_ord - ord('a') + 1] = chr(ch_ord)

        ans = ''
        while n > 0:
            num = max(k - 26 * (n - 1), 1)
            ans += num_val[num]

            k -= num
            n -= 1

        return ans