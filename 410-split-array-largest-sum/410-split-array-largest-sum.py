class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high)//2
            tot_sum_of_part, cnt = 0, 1
            for num in nums:
                if tot_sum_of_part + num <= mid: 
                    tot_sum_of_part += num
                else:
                    tot_sum_of_part = num
                    cnt += 1
                    
            if cnt > m:     # there are more than m subbarays with mid sum, we can increase mid
                low = mid + 1          
            else:           # sum 
                high = mid
                
        return high
            
        
        