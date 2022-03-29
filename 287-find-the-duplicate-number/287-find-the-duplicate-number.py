class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low <= high:
            mid, cnt = low + (high - low) // 2, 0

            for n in nums:
                if n <= mid:
                    cnt += 1
            print(low, mid, high, cnt)
            if cnt <= mid:
                low = mid + 1
            else:
                high = mid - 1

        return low