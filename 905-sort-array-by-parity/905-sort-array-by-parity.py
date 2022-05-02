class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return list(filter(lambda p : p%2 == 0, nums)) + list(filter(lambda p : p%2 != 0, nums))