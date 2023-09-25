from functools import reduce

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(lambda a, b: a ^ ord(b), list(s+t), 0))
