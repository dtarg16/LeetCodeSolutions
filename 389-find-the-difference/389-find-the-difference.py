class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        res = ord(t[-1])
        for i in range(len(s)):
            res ^= ord(s[i]) ^ ord(t[i])

        return chr(res)