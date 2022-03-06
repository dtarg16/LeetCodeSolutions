from bisect import bisect_left ,bisect
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans = k * (k + 1) // 2
        level = k + 1
        
        for x in sorted(set(nums)):
            if x < level:
                ans += level - x
                level += 1
        return ans