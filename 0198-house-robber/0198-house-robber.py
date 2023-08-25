class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[-1 for _ in range(len(nums))]

        def rec(i):
            if i<0:
                return 0
            
            if memo[i] >= 0:
                return  memo[i]

            memo[i]=max(rec(i-2) + nums[i], rec(i-1))
            return memo[i]
        
        return rec(len(nums)-1)