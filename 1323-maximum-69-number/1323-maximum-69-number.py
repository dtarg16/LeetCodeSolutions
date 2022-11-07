class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = str(num)
        j = 1
        for i in range(len(nums)):
            if nums[i] == "6" and (j == 1):
                bef = nums[:i]
                aft = nums[i+1:]
                nums = bef + "9"+aft
                j-=1
        nums = int(nums)
        return nums