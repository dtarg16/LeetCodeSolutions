class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left, right, maxx = 0, 0, 0

        while right < len(nums):
            while max_deque and nums[right] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[right])

            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[right])

            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1

            maxx = max(maxx, right - left + 1)
            right +=1

        return maxx