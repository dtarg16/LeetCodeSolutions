class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            right_most_bit = n & 1
            n >>= 1 # shift n's bit to the right
            res <<= 1 # shift res bits to the left
            res ^= right_most_bit
        return res