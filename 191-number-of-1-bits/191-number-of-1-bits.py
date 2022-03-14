class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([int(ch) for ch in bin(n)[2::]])