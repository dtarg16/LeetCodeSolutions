class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left = 0
        for i in range(len(nums)):
            x = nums[i]
            if x != val:
                nums[left] = x
                left += 1
        return left