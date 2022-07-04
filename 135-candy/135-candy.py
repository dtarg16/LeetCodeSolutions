class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n
        
        nums = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1


        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                nums[i-1] = max(nums[i]+1, nums[i-1])
   
        return sum(nums)