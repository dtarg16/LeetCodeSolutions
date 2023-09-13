class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        @cache
        def lcs(l: int, r: int) -> int:
            if l >= n or r < 0:
                return 0
            if s[l] == s[r]:
                return 1 + lcs(l + 1, r - 1)

            return max(lcs(l + 1, r), lcs(l, r - 1))

        return lcs(0, n-1)