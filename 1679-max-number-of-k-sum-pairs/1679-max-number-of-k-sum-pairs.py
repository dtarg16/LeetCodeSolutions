class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        ans = 0
        for num in nums:
            count = d.get(k - num, 0)
            if count > 0:
                ans += 1
                d[k - num] = count - 1
            else:
                d[num] = d.get(num, 0) + 1
                
        return ans