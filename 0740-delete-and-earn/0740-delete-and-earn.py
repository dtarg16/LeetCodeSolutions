class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if  not nums:
            return 0

        freq = [0] * (max(nums)+1)
        for n in nums:
            freq[n] += n


        def dp(nums):
            memo=[-1 for _ in range(len(nums))]
            def rec(i):
                if i<0:
                    return 0
                
                if memo[i] >= 0:
                    return  memo[i]

                memo[i]=max(rec(i-2) + nums[i], rec(i-1))
                return memo[i]
            
            return rec(len(nums)-1)
        
        return dp(freq)