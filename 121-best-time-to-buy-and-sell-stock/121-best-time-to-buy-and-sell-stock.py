class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_so_far = prices[0]
        maxx = 0
        for i in range(1, len(prices)):
            price = prices[i]
            min_so_far = min(min_so_far, price)
            maxx = max(maxx, price - min_so_far)

        return maxx