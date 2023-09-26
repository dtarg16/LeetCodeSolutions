class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter = collections.Counter(list(s))
        res = []
        for _ in range(counter["1"] - 1):
            res.append("1")

        for _ in range(counter["0"]):
            res.append("0")

        res.append("1")

        return "".join(res)