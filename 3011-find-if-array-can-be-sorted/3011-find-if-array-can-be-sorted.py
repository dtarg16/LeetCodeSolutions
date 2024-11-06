class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        previous_max = current_min = current_max = previous_count = 0
        for num in nums:
            current_count = num.bit_count()
            if previous_count == current_count:
                current_min = min(current_min, num)
                current_max = max(current_max, num)
            elif current_min < previous_max:
                return False
            else:
                previous_max = current_max
                current_min = current_max = num
                previous_count = current_count
        return current_min >= previous_max
