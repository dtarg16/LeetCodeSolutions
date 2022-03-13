class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k%2 == 1 and len(nums) == 1:
            return -1
        maxx = -1
        
        if k == 0 and len(nums) > 0:
            return nums[0]

        while k>1:
            if not nums:
                return maxx
            k -= 1
            top = nums.pop(0)
            maxx = max(maxx, top)

        if len(nums)>1:
            return max(maxx, nums[1])
        return maxx