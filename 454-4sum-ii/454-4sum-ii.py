class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        ans = 0
        d = {}
        for x in nums1:
            for y in nums2:
                d[x+y] = d.get(x+y, 0) + 1
                
        for x in nums3:
            for y in nums4:
                ans += d.get(-(x+y), 0)
                
        return ans