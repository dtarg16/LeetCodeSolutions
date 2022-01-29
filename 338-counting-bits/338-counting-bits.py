class Solution(object):
    
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)
            
        for i in range(n + 1):
            if(i % 2 == 0):
                ans[i] = ans[i/2]
            else:
                ans[i] = ans[i/2] + 1
        return ans