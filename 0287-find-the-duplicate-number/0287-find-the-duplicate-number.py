class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = 0
        for num in nums:
            mask = 1 << num
            if visited & mask:
                return num
            visited |= mask