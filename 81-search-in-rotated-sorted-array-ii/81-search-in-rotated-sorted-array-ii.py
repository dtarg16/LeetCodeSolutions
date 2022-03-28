class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return nums[0] == target

        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] and nums[right] == nums[mid]:
                left += 1
                right -= 1

            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False