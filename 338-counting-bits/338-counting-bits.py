class Solution(object):
    def rec(self, n):
        if n in self.dp:
            return self.dp[n]
        if n <= 1:
            return n

        count = self.rec(n >> 1)
        if n % 2 == 1:
            count += 1

        self.dp[n] = count
        return count

    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.dp = {}
        ans = []
        for i in range(n + 1):
            ans.append(self.rec(i))
        return ans