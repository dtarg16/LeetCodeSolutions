class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter = 0
        maxx = 0
        d = {0: -1}
        for i in range(len(nums)):
            num = nums[i]
            if num:
                counter += 1
            else:
                counter -= 1

            prev_counter_index = d.get(counter, i)
            maxx = max(maxx, i - prev_counter_index)
            d[counter] = min(prev_counter_index, i)

        return maxx