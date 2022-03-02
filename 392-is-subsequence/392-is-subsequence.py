class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, k = 0, 0

        while i < len(t) and k < len(s):
            if s[k] == t[i]:
                k += 1
            i += 1
        return k == len(s)