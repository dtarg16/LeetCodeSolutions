class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0        
        for i in range(32):
            right_bit = n & 1
            n >>= 1;
            ans += right_bit
        return ans