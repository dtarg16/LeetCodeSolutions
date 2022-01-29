class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self
        ans = []
        for i in range(n+1):
            ans.append((bin(i)[2::]).count('1'))
        return ans