from heapq import heappush, heappop

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        ans = -float("inf")
        cumsum = [0] + list(accumulate(nums))
        dic = {c:i for i,c in enumerate(cumsum)}
        goal = cumsum[-1] - x

        if goal < 0: 
            return -1

        for num in dic:
            if num + goal in dic:
                ans = max(ans, dic[num + goal] - dic[num])
        
        if ans != -float("inf"):
            return len(nums) - ans
        
        return -1

            
        
        