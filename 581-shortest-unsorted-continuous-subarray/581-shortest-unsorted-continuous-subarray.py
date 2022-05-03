class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right , minn, maxx = -1, -2, nums[-1], nums[0]
        for i in range(len(nums)):
            maxx = max(maxx, nums[i])
            minn = min(minn, nums[-(1+i)])
            if nums[i] < maxx:
                right = i
            if nums[-(1+i)] > minn:
                left = len(nums)-1-i
                
        return right - left + 1
                
                
            