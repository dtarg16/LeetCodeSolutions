class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def num_set_bits(num):
            return sum([int(bit) for bit in bin(num)[2:]])

        left, right = 0, 0
        while right < len(nums):
            if num_set_bits(nums[left]) != num_set_bits(nums[right]):
                nums[left:right] = sorted(nums[left:right])
                left = right
            else:
                right += 1

        nums[left:right] = sorted(nums[left:right])
        return list(sorted(nums)) == nums
