class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length=len(nums) 
        sum_nums = length*(length+1)//2 
        repetition = sum(nums) - sum(set(nums))
        loss = sum_nums - sum(set(nums))
        print(sum(set(nums)))
        return [repetition,loss]