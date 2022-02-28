class Solution:
    def range_to_str(self, beg, end):
        if beg == end:
            return str(beg)
        else:
            return str(beg) + "->" + str(end)
    
    def summaryRanges(self, nums: List[int]) -> List[str]:
        end, result, N = 0, [], len(nums)
        
        while end < N:
            beg = end
            while end < N - 1 and nums[end] + 1 == nums[end + 1]: 
                end += 1
            result.append(self.range_to_str(nums[beg],nums[end]))     
            end +=  1
        
        return result
            